import os
from functools import cached_property

from utils_future import JSONFile, Log

log = Log("TableNormalizedDataMixin")


class TableNormalizedDataMixin:
    @cached_property
    def normalized_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "normalized_data.json"))

    def build_normalized_data(self, force=False):
        if self.normalized_data_file.exists and not force:
            return

        data = self.get_data()

        primary_keys = data["primary_keys"]
        field_keys = data["field_keys"]

        normalized_data_list = []
        for row in data["rows"]:
            normalized_data = {}
            values = {}
            for k in primary_keys:
                normalized_data[k] = row[k]
            for k in field_keys:
                values[k] = row["values"][k]
            normalized_data["values"] = values
            normalized_data_list.append(normalized_data)

        self.normalized_data_file.write(normalized_data_list)
        log.info(
            f"Wrote {len(normalized_data_list)}"
            + f" rows to {self.normalized_data_file}."
        )

    def get_normalized_data_list(self):
        return self.normalized_data_file.read()
