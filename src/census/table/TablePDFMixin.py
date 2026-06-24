import os
from functools import cached_property

from utils_future import Log, PDFFile

log = Log("TablePDFMixin")


class TablePDFMixin:
    PAGE_NO_OFFSET = 13

    @cached_property
    def dir_data(self) -> str:
        dir_data = os.path.join(
            "data", "tables", self.table_group_id, self.table_id
        )
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @cached_property
    def pdf_file(self):
        return PDFFile(os.path.join(self.dir_data, "original.pdf"))

    @cached_property
    def actual_page_no(self) -> int:
        return self.doc_page_no + self.PAGE_NO_OFFSET

    def build_pdf(self, force=False):
        if self.pdf_file.exists and not force:
            return

        self.CLEANED_ORIGINAL_PDF_FILE.extract_pages(
            [self.actual_page_no - 1], self.pdf_file
        )
        log.info(f"Wrote {self.pdf_file}.")
