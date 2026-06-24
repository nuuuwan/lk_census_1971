from census.table import Table
from utils_future import File, Log

log = Log("OriginalDocReadmeMixin")


class ReadMe:
    README_FILE = File("README.md")

    @staticmethod
    def lines_for_header() -> list[str]:
        return [
            "![CPH](https://img.shields.io/badge/CPH-1971-blue)",
            "",
            "---",
            "",
        ]

    @staticmethod
    def lines_for_footer() -> list[str]:
        return [
            "---",
            "",
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
            "",
        ]

    @classmethod
    def build(cls):
        tables = Table.list()
        n_tables = len(tables)
        tables_by_group = Table.list_by_group()
        lines = (
            [
                "# Sri Lanka 🇱🇰  - Census of Population 1971",
                "",
            ]
            + cls.lines_for_header()
            + [
                f"Structured data extracted from **{n_tables}** Tables.",
                "",
                "*Source: [Census of Population 1971, Sri Lanka - Report]"
                + "(original_data/Census1971_Report.pdf)*",
                "",
            ]
        )

        for group_id, group_tables in tables_by_group.items():
            lines.extend([f"## {group_id[6:]}", ""])
            for table in group_tables:
                lines.append(
                    f"- {
                        table.table_no}: [{
                        table.table_name}]({
                        table.dir_data})"
                )
            lines.append("")

        lines.extend(cls.lines_for_footer())

        cls.README_FILE.write("\n".join(lines))
        log.debug(f"Wrote {cls.README_FILE}")
