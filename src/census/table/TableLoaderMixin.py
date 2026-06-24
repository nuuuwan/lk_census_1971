from utils_future import Log

log = Log('TableLoaderMixin')


class TableLoaderMixin:
    @classmethod
    def from_dict(cls, d):
        return cls(
            table_no=d['table_no'],
            table_name=d['table_name'],
            doc_page_no=d['doc_page_no'],
        )

    @classmethod
    def list(cls):
        metadata = cls.load_metadata()
        tables = [cls.from_dict(d) for d in metadata]
        log.debug(f'Loaded {len(tables)} tables')
        return tables
