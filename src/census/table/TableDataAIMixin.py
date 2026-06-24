import base64
import json
import mimetypes
import os
import time
from functools import cached_property

import anthropic

from utils_future import File, Log

log = Log("TableDataAIMixin")


class TableDataAIMixin:
    AI_MODEL = "claude-opus-4-6"
    AI_MODEL_URL = "https://www.anthropic.com/claude/opus"
    AI_MAX_TOKENS = 8192

    PROMPT_FILE = File(os.path.join("src", "census", "table", "prompt.txt"))

    @cached_property
    def ai_client(self):
        return anthropic.Anthropic()

    def _build_image_blocks(self):
        blocks = []
        for image_file in self.get_image_files():
            media_type = (
                mimetypes.guess_type(image_file.path)[0] or "image/png"
            )
            with open(image_file.path, "rb") as f:
                b64 = base64.standard_b64encode(f.read()).decode("utf-8")
            blocks.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": b64,
                    },
                }
            )
        return blocks

    def extract_data_with_ai(self):
        log.debug(
            f"🤖 Extracting data from {self}"
            + f" using {self.AI_MODEL} ({self.AI_MAX_TOKENS} tokens)."
        )
        t_start = time.time()
        extraction_prompt = self.PROMPT_FILE.read()
        content = self._build_image_blocks()
        content.append(
            {
                "type": "text",
                "text": extraction_prompt.format(
                    table_no=self.table_no,
                    table_name=self.table_name,
                ),
            }
        )

        msg = self.ai_client.messages.create(
            model=self.AI_MODEL,
            max_tokens=self.AI_MAX_TOKENS,
            messages=[{"role": "user", "content": content}],
        )

        raw = "".join(b.text for b in msg.content if b.type == "text").strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1].lstrip("json").strip()
        data = json.loads(raw)

        if not data.get("found"):
            raise ValueError(
                f"Error. Table '{self.table_no}'"
                + f" not found on page {self.doc_page_no}."
            )

        dt = time.time() - t_start
        log.debug(f"Table {self.table_no} completed in {dt:.1f}s.")
        return data
