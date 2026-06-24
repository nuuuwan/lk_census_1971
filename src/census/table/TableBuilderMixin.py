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

        tables = cls.list()
        for table in tables[:1]:
            table.build()
            log.debug("Building {table} complete.")
            log.debug("-" * 40)
