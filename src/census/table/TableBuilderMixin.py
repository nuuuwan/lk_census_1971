class TableBuilderMixin:
    def build(self):
        pass

    @classmethod
    def build_all(cls):
        tables = cls.list()
        for table in tables:
            table.build()
