from utils_future import Log

log = Log("TablePreDocsMixin")


class TablePreDocsMixin:

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

    @classmethod
    def build_pre_docs(cls):
        cls.clean_original_report()
        cls.extract_list_of_tables()
