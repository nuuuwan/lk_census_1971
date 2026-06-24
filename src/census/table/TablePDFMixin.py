import os
from functools import cached_property

from utils_future import File


class TablePDFMixin:
    @cached_property
    def dir_data(self) -> str:
        dir_data = os.path.join('data', 'tables', self.table_id)
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @cached_property
    def pdf_file(self):
        return File(os.path.join(self.dir_data, "table.pdf"))

    def build_pdf(self):
        pass
