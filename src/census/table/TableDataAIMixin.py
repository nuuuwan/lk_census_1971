import base64
import json
import mimetypes
import os
from functools import cached_property

import anthropic

from utils_future import File, Log

log = Log("TableDataAIMixin")


class TableDataAIMixin:
    AI_MODEL = "claude-opus-4-6"
    AI_MAX_TOKENS = 8192

    PROMPT_FILE = File(os.path.join("src", "census", "table", "prompt.txt"))

    @cached_property
    def ai_client(self):
        return anthropic.Anthropic()

    def _build_image_blocks(self):
        blocks = []
        for image_path in self.get_image_paths():
            media_type = mimetypes.guess_type(image_path)[0] or "image/png"
            with open(image_path, "rb") as f:
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
            log.warning(
                f"Table '{
                    self.table_no}' not found on page {
                    self.doc_page_no}."
            )

        return data
