from census.table.TableBase import TableBase
from census.table.TableBuilderMixin import TableBuilderMixin
from census.table.TableLoaderMixin import TableLoaderMixin
from census.table.TableMetadataMixin import TableMetadataMixin


class Table(
    TableBase, TableMetadataMixin, TableLoaderMixin, TableBuilderMixin
):
    pass
