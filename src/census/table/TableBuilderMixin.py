from utils_future import Log

log = Log("TableBuilderMixin")


class TableBuilderMixin:
    def build(self):
        self.build_pdf()
        self.build_images()
        self.build_data()
        self.build_readme()

    @classmethod
    def build_all(cls):
        cls.clean_original_report()
        cls.extract_list_of_tables()
        log.debug("...")

        tables = cls.list()
        n_tables = len(tables)
        for i_table, table in enumerate(tables, start=1):
            log.debug("-" * 40)
            log.debug(f"{i_table}/{n_tables} {table}.")
            log.debug("-" * 40)
            table.build()

        log.debug("...")
