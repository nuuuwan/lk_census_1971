from census.table.TableBase import TableBase
from census.table.TableBuilderMixin import TableBuilderMixin
from census.table.TableDataMixin import TableDataMixin
from census.table.TableLoaderMixin import TableLoaderMixin
from census.table.TableMetadataMixin import TableMetadataMixin
from census.table.TablePDFMixin import TablePDFMixin
from census.table.TableReadMeMixin import TableReadMeMixin


class Table(
    TableBase,
    TableMetadataMixin,
    TableLoaderMixin,
    TableBuilderMixin,
    TablePDFMixin,
    TableDataMixin,
    TableReadMeMixin,
):
    pass
