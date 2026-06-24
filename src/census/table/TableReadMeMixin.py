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
        image_paths = self.get_image_paths()
        lines = [
            f"## Original Table [Image](../../../../{image_paths[0]})",
            "",
            f"![](../../../../{image_paths[0]})",
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

    def lines_for_files(self) -> list[str]:
        lines = []
        for label, file in [
            ("📜 Original PDF", self.pdf_file),
            ("📜 Original Image", File(self.get_image_paths()[0])),
            ("📄 Extracted JSON Data", self.data_file),
            ("📄 README", self.readme_file),
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
            + self.lines_for_json()
            + self.lines_for_image()
            + ReadMe.lines_for_footer()
        )
        self.readme_file.write("\n".join(lines))
        log.info(f"Wrote {self.readme_file}")
