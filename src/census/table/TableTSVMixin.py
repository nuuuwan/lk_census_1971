import os
from functools import cached_property

from utils_future import Log, TSVFile

log = Log("TableTSVMixin")


class TableTSVMixin:
    @cached_property
    def tsv_file(self):
        return TSVFile(os.path.join(self.dir_data, "data.tsv"))

    def get_tsv_data(self, normalized_data):
        tsv_data = {}
        for k, v in normalized_data.items():
            if k != "values":
                tsv_data[k] = v

        tsv_data |= normalized_data["values"]
        return tsv_data

    def build_tsv(self, force=True):
        if self.tsv_file.exists and not force:
            return

        normalized_data_list = self.get_normalized_data_list()
        tsv_data_list = [self.get_tsv_data(d) for d in normalized_data_list]
        self.tsv_file.write(tsv_data_list)
        log.info(f"Wrote {len(tsv_data_list)} rows to {self.tsv_file}.")
