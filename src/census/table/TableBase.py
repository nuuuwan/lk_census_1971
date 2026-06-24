from dataclasses import dataclass


@dataclass
class TableBase:
    table_no: str
    table_name: str
    doc_page_no: int
