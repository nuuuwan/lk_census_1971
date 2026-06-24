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
        ]

    @staticmethod
    def lines_for_footer() -> list[str]:
        return [
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
            "",
        ]

    @classmethod
    def lines_for_tables(cls):
        lines = [
            "## Tables",
            "",
        ]
        tables_by_group = Table.list_by_group()
        for group_id, group_tables in tables_by_group.items():
            lines.extend([f"### {group_id[6:]}.x", ""])
            for table in group_tables:
                lines.append(f"- {
                        table.table_no}: [{
                        table.table_name}]({
                        table.dir_data})")
            lines.append("")
        return lines

    @classmethod
    def build(cls):
        tables = Table.list()
        n_tables = len(tables)

        lines = (
            [
                "# Sri Lanka 🇱🇰  - Census of Population 1971",
                "",
            ]
            + cls.lines_for_header()
            + [
                "This repo contains structured data from the"
                + " **Census of Population 1971, Sri Lanka.**",
                "",
                " The data was extracted from the"
                + " *[General Report](original_data/Census1971_Report.pdf)*,"
                + " published by the"
                + " [Department of Census and Statistics, Sri Lanka]"
                + "(https://www.statistics.gov.lk/), "
                + f"and covers **{n_tables}** tables, extracted using"
                + f" [{Table.AI_MODEL}]({Table.AI_MODEL_URL})"
                + f" ({Table.AI_MAX_TOKENS} tokens,"
                + f" [prompt]({Table.PROMPT_FILE.path})).",
                "",
            ]
            + cls.lines_for_tables()
            + cls.lines_for_footer()
        )

        cls.README_FILE.write("\n".join(lines))
        log.debug(f"Wrote {cls.README_FILE}")
