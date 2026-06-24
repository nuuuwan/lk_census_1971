import json
import os
from functools import cached_property

from utils_future import File, Log

log = Log("TableReadMeMixin")


class TableReadMeMixin:
    @cached_property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    def lines_for_image(self) -> list[str]:
        first_image_file = self.first_image_file
        lines = [
            f"## Original Table [Image](../../../../{first_image_file.path})",
            "",
            f"<img src='../../../../{first_image_file.path}'"
            + f" alt='Table {self.table_no} Image' width='640px' />",
            "",
        ]
        return lines

    def lines_for_json(self) -> list[str]:
        lines = [
            f"## Extracted [JSON Data](../../../../{self.data_file.path})",
            "",
        ]

        data = self.get_data()
        if data:
            lines += ["```json"]
            lines += [json.dumps(data, indent=4)]
            lines += ["```", ""]
        else:
            lines += ["*⚠️ No data extracted yet.*"]
        return lines

    def lines_for_tsv(self) -> list[str]:
        lines = [
            f"## Extracted [TSV Data](../../../../{self.tsv_file.path})",
            "",
        ]

        if not self.tsv_file.exists:
            lines += ["*⚠️ No data extracted yet.*"]
            return lines

        rows = self.tsv_file.read()
        if not rows:
            lines += ["*⚠️ No data extracted yet.*"]
            return lines

        headers = list(rows[0].keys())
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in rows:
            lines.append(
                "| " + " | ".join(str(row.get(h, "")) for h in headers) + " |"
            )
        lines.append("")
        return lines

    def lines_for_files(self) -> list[str]:
        lines = []
        for label, file in [
            ("📜 Original Table PDF", self.pdf_file),
            ("📜 Original Table Image", self.first_image_file),
            ("📄 Extracted JSON Data", self.data_file),
            ("📄 Extracted TSV Data", self.tsv_file),
        ]:
            if file.exists:
                lines.append(f"- {label} - [{file}](../../../../{file.path})")
        lines.append("")
        return lines

    def build_readme(self, force=True):
        from census.readme.ReadMe import ReadMe

        if self.readme_file.exists and not force:
            return
        lines = (
            [f"# {self.table_no}: {self.table_name}", ""]
            + ReadMe.lines_for_header()
            + self.lines_for_files()
            + self.lines_for_image()
            + self.lines_for_json()
            + self.lines_for_tsv()
            + ReadMe.lines_for_footer()
        )
        self.readme_file.write("\n".join(lines))
        log.info(f"Wrote {self.readme_file}")
