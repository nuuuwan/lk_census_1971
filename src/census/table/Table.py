from census.table.TableBase import TableBase
from census.table.TableBuilderMixin import TableBuilderMixin
from census.table.TableDataMixin import TableDataMixin
from census.table.TableLoaderMixin import TableLoaderMixin
from census.table.TableMetadataMixin import TableMetadataMixin
from census.table.TablePDFMixin import TablePDFMixin


class Table(
    TableBase,
    TableMetadataMixin,
    TableLoaderMixin,
    TableBuilderMixin,
    TablePDFMixin,
    TableDataMixin,
):
    pass
