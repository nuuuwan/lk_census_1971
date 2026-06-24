import os
from functools import cached_property

from utils_future import Log, TSVFile

log = Log("TableTSVMixin")


class TableTSVMixin:
    @cached_property
    def tsv_file(self):
        return TSVFile(os.path.join(self.dir_data, "data.tsv"))

    def get_tsv_data_list(self, data):
        assert data.get(
            "found"
        ), f"Data file {self.data_file} does not contain valid data."

        primary_keys = data["primary_keys"]
        field_keys = data["field_keys"]

        tsv_data_list = []
        for row in data["rows"]:
            tsv_data = {}
            for k in primary_keys:
                tsv_data[k] = row[k]
            for k in field_keys:
                tsv_data[k] = row["values"][k]
            tsv_data_list.append(tsv_data)

        return tsv_data_list

    def build_tsv(self, force=False):
        if self.tsv_file.exists and not force:
            return

        data = self.get_data()
        tsv_data_list = self.get_tsv_data_list(data)
        self.tsv_file.write(tsv_data_list)
        log.info(f"Wrote {len(tsv_data_list)} rows to {self.tsv_file}.")
