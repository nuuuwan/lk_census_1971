class TableBuilderMixin:
    def build(self):
        self.build_pdf()

    @classmethod
    def build_all(cls):
        tables = cls.list()
        for table in tables:
            table.build()
