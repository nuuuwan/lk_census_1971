import os
from functools import cached_property

from utils_future import Log, TSVFile

log = Log("TableTSVMixin")


class TableTSVMixin:
    @cached_property
    def tsv_file(self):
        return TSVFile(os.path.join(self.dir_data, "data.tsv"))

    def build_tsv(self, force=False):
        if self.tsv_file.exists and not force:
            return
