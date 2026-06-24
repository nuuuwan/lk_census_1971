import fitz

from utils_future.console.Log import Log
from utils_future.file.File import File

log = Log("PDFFile")


class PDFFile(File):

    def extract_pages(
        self, page_numbers: list[int], output_pdf_file: "PDFFile"
    ) -> None:
        with fitz.open(self.path) as pdf:
            new_pdf = fitz.open()
            for page_number in page_numbers:
                if page_number < 0 or page_number >= len(pdf):
                    raise ValueError(
                        f"Page number {page_number} is out of range"
                    )
                new_pdf.insert_pdf(
                    pdf, from_page=page_number, to_page=page_number
                )
            new_pdf.save(output_pdf_file.path)
            log.debug(
                f"Extracted pages {page_numbers}"
                + f" from {self} to {output_pdf_file}."
            )
