import fitz

from utils_future.console.Log import Log
from utils_future.file.File import File

log = Log("PDFFile")


class PDFFile(File):

    def extract_page(self, page_no: int, output_path: str) -> None:
        with fitz.open(self.path) as pdf:
            if page_no < 0 or page_no >= len(pdf):
                raise ValueError(
                    f"Page number {page_no} is out of range for this PDF."
                )
            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf, from_page=page_no, to_page=page_no)
            new_pdf.save(output_path)
            log.debug(
                f"Extracted page {page_no}"
                + f" from {self} to {PDFFile(output_path)}."
            )
