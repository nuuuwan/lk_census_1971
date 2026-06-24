import os
from functools import cached_property

from utils_future import Log, PDFFile

log = Log("TablePDFMixin")


class TablePDFMixin:
    PAGE_NO_OFFSET = 13
    ORIGINAL_PDF_FILE = PDFFile(
        os.path.join("original_data", "Census1971_Report.pdf")
    )
    CLEANED_ORIGINAL_PDF_FILE = PDFFile(
        os.path.join("data", "lk_census1971.original_report.cleaned.pdf")
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

        self.CLEANED_ORIGINAL_PDF_FILE.extract_pages(
            [self.actual_page_no - 1], self.pdf_file
        )
        log.info(f"Wrote {self.pdf_file}.")

    @classmethod
    def clean_original_report(cls):
        if cls.CLEANED_ORIGINAL_PDF_FILE.exists:
            log.debug(f"{cls.CLEANED_ORIGINAL_PDF_FILE} exists.")
            return

        page_numbers = list(range(0, 56)) + list(range(58, 231))
        cls.ORIGINAL_PDF_FILE.extract_pages(
            page_numbers, cls.CLEANED_ORIGINAL_PDF_FILE
        )
        log.info(f"Wrote {cls.CLEANED_ORIGINAL_PDF_FILE}.")

    @classmethod
    def extract_list_of_tables(cls):
        if cls.LIST_OF_TABLES_PDF_FILE.exists:
            log.debug(f"{cls.LIST_OF_TABLES_PDF_FILE} exists.")
            return

        cls.CLEANED_ORIGINAL_PDF_FILE.extract_pages(
            list(
                range(
                    cls.LIST_OF_TABLES_FROM_PAGE - 1,
                    cls.LIST_OF_TABLES_TO_PAGE,
                )
            ),
            cls.LIST_OF_TABLES_PDF_FILE,
        )
        log.info(f"Wrote {cls.LIST_OF_TABLES_PDF_FILE}.")
