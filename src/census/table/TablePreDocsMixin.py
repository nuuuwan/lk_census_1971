import os

from utils_future import File, Log, PDFFile

log = Log("TablePreDocsMixin")


class TablePreDocsMixin:
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

    TITLE_PAGE_PDF_FILE = PDFFile(
        os.path.join("data", "lk_census1971.title_page.pdf")
    )

    INDEX_PAGE_PDF_FILE = PDFFile(
        os.path.join("data", "lk_census1971.index_page.pdf")
    )

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
    def extract_title_page(cls):
        if cls.TITLE_PAGE_PDF_FILE.exists:
            log.debug(f"{cls.TITLE_PAGE_PDF_FILE} exists.")
            return

        cls.CLEANED_ORIGINAL_PDF_FILE.extract_pages(
            [0], cls.TITLE_PAGE_PDF_FILE
        )
        log.info(f"Wrote {cls.TITLE_PAGE_PDF_FILE}.")

        cls.TITLE_PAGE_PDF_FILE.extract_images()
        log.info(f"Wrote images from {cls.TITLE_PAGE_PDF_FILE}.")

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

    @classmethod
    def extract_index_page(cls):
        if cls.INDEX_PAGE_PDF_FILE.exists:
            log.debug(f"{cls.INDEX_PAGE_PDF_FILE} exists.")
            return

        cls.LIST_OF_TABLES_PDF_FILE.extract_pages(
            [0], cls.INDEX_PAGE_PDF_FILE
        )
        log.info(f"Wrote {cls.INDEX_PAGE_PDF_FILE}.")

        cls.INDEX_PAGE_PDF_FILE.extract_images()
        log.info(f"Wrote images from {cls.INDEX_PAGE_PDF_FILE}.")

    @classmethod
    def build_pre_docs(cls):
        cls.clean_original_report()
        cls.extract_title_page()
        cls.extract_list_of_tables()
        cls.extract_index_page()

    @classmethod
    def get_title_page_first_image_file(cls):
        return File(
            os.path.join(
                cls.TITLE_PAGE_PDF_FILE.path[:-4] + ".images", "image-01.png"
            )
        )

    @classmethod
    def get_index_page_first_image_file(cls):
        return File(
            os.path.join(
                cls.INDEX_PAGE_PDF_FILE.path[:-4] + ".images", "image-01.png"
            )
        )
