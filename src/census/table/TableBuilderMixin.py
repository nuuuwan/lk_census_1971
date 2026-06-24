from utils_future import Log

log = Log("TableBuilderMixin")


class TableBuilderMixin:
    def build(self):
        self.build_pdf()
        self.build_data()

    @classmethod
    def build_all(cls):
        cls.clean_original_report()
        cls.extract_list_of_tables()
        log.debug("-" * 40)

        tables = cls.list()
        for table in tables[:1]:
            table.build()
            log.debug(f"Building {table} complete.")
            log.debug("-" * 40)
