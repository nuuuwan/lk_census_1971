import os
from functools import cached_property

from utils_future import Log, PDFFile

log = Log("TablePDFMixin")


class TablePDFMixin:
    PAGE_NO_OFFSET = 13
    ORIGINAL_PDF_FILE = PDFFile(
        os.path.join("original_data", "Census1971_Report.pdf")
    )
    LIST_OF_TABLES_PDF_FILE = PDFFile(
        os.path.join("data", "list_of_tables.pdf")
    )
    LIST_OF_TABLES_FROM_PAGE = 8
    LIST_OF_TABLES_TO_PAGE = 11

    @cached_property
    def dir_data(self) -> str:
        dir_data = os.path.join(
            "data", "tables", self.table_group_id, self.table_id
        )
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @cached_property
    def pdf_file(self):
        return PDFFile(os.path.join(self.dir_data, "table.pdf"))

    @cached_property
    def actual_page_no(self) -> int:
        return self.doc_page_no + self.PAGE_NO_OFFSET

    def build_pdf(self, force=False):
        if self.pdf_file.exists and not force:
            log.debug(f"{self.pdf_file} exists.")
            return

        self.ORIGINAL_PDF_FILE.extract_page(
            self.actual_page_no - 1,
            self.actual_page_no - 1,
            self.pdf_file.path,
        )
        log.info(f"Wrote {self.pdf_file}.")

    @classmethod
    def extract_list_of_tables(cls):
        cls.ORIGINAL_PDF_FILE.extract_page(
            cls.LIST_OF_TABLES_FROM_PAGE - 1,
            cls.LIST_OF_TABLES_TO_PAGE - 1,
            cls.LIST_OF_TABLES_PDF_FILE.path,
        )
        log.info(f"Wrote {cls.LIST_OF_TABLES_PDF_FILE}.")
