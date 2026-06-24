from census.table.TableBase import TableBase
from census.table.TableBuilderMixin import TableBuilderMixin
from census.table.TableDataMixin import TableDataMixin
from census.table.TableImageMixin import TableImageMixin
from census.table.TableLoaderMixin import TableLoaderMixin
from census.table.TableMetadataMixin import TableMetadataMixin
from census.table.TableNormalizedDataMixin import TableNormalizedDataMixin
from census.table.TablePDFMixin import TablePDFMixin
from census.table.TablePreDocsMixin import TablePreDocsMixin
from census.table.TableReadMeMixin import TableReadMeMixin
from census.table.TableTSVMixin import TableTSVMixin


class Table(
    TableBase,
    TableMetadataMixin,
    TableLoaderMixin,
    #
    TableBuilderMixin,
    TablePreDocsMixin,
    TablePDFMixin,
    TableImageMixin,
    TableDataMixin,
    TableNormalizedDataMixin,
    TableTSVMixin,
    #
    TableReadMeMixin,
):
    pass
