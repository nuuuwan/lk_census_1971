from dataclasses import dataclass
from functools import cached_property


@dataclass
class TableBase:
    table_no: str
    table_name: str
    doc_page_no: int

    @cached_property
    def table_id(self) -> str:
        part1, part2 = self.table_no.split(".")
        part1 = int(part1)
        part2 = int(part2)
        return f"table-{part1:01d}-{part2:02d}"

    @cached_property
    def table_group_id(self) -> str:
        return self.table_id[:7]

    def __str__(self) -> str:
        return f"Table({self.table_no})"

    def __repr__(self) -> str:
        return self.__str__()
