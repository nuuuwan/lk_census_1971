import os
from functools import cached_property

from census.table.TableDataAIMixin import TableDataAIMixin
from utils_future import JSONFile, Log

log = Log("TableDataMixin")


class TableDataMixin(TableDataAIMixin):

    @cached_property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    def build_data(self, force=False):
        if self.data_file.exists and not force:
            return
        data = self.extract_data_with_ai()

        if data.get("found"):
            self.data_file.write(data)
            log.info(f"Wrote {self.data_file}.")

    def get_data(self):
        if not self.data_file.exists:
            return None
        data = self.data_file.read()
        assert data.get(
            "found"
        ), f"Data file {self.data_file} does not contain valid data."
        return data
