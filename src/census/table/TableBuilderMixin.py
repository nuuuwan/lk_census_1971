class TableBuilderMixin:
    def build(self):
        self.build_pdf()

    @classmethod
    def build_all(cls):
        cls.extract_list_of_tables()

        tables = cls.list()
        for table in tables:
            table.build()
