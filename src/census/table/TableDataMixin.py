import os
from functools import cached_property

from utils_future import JSONFile, Log

log = Log("TableDataMixin")


class TableDataMixin:
    @cached_property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    def extract_data_with_ai(self):
        return {}

    def build_data(self, force=True):
        if self.data_file.exists and not force:
            return
        data = self.extract_data_with_ai()
        self.data_file.write(data)
        log.info(f"Wrote {self.data_file}.")
