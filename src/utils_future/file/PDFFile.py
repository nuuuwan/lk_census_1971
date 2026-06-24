import fitz

from utils_future.console.Log import Log
from utils_future.file.File import File

log = Log("PDFFile")


class PDFFile(File):

    def extract_page(
        self, from_page: int, to_page: int, output_path: str
    ) -> None:
        with fitz.open(self.path) as pdf:
            if from_page < 0 or to_page >= len(pdf) or from_page > to_page:
                raise ValueError(
                    f"Page numbers {from_page} to {to_page}"
                    + " are out of range for this PDF."
                )
            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf, from_page=from_page, to_page=to_page)
            new_pdf.save(output_path)
            log.debug(
                f"Extracted pages {from_page} to {to_page}"
                + f" from {self} to {PDFFile(output_path)}."
            )
