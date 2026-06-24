from functools import cache

from utils_future import Log

log = Log("TableLoaderMixin")


class TableLoaderMixin:
    @classmethod
    def from_dict(cls, d):
        return cls(
            table_no=d["table_no"],
            table_name=d["table_name"],
            doc_page_no=d["doc_page_no"],
        )

    @classmethod
    def validate_tables(cls, tables):
        prev_doc_page_no = None
        for table in tables:
            if (
                prev_doc_page_no is not None
                and table.doc_page_no < prev_doc_page_no
            ):
                raise ValueError(
                    f"Table {table.table_no}"
                    + f" has doc_page_no {table.doc_page_no}, "
                    + "which is less than than previous table's"
                    + f" doc_page_no {prev_doc_page_no}"
                )
            prev_doc_page_no = table.doc_page_no

    @classmethod
    @cache
    def list(cls):
        metadata = cls.load_metadata()
        tables = [cls.from_dict(d) for d in metadata]
        log.debug(f"Loaded {len(tables)} tables")
        return tables

    @classmethod
    @cache
    def list_by_group(cls):
        tables = cls.list()
        grouped_tables = {}
        for table in tables:
            table_group_id = table.table_group_id
            if table_group_id not in grouped_tables:
                grouped_tables[table_group_id] = []
            grouped_tables[table_group_id].append(table)
        return grouped_tables
