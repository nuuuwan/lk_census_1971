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
            log.info(
                f"Wrote {output_pdf_file} with extracted pages {page_numbers}"
                + f" from {self}."
            )

    def extract_images(self):
        assert self.path.endswith(".pdf"), "File must be a PDF"
        with fitz.open(self.path) as pdf:
            for page_number, page in enumerate(pdf):
                image_list = page.get_images(full=True)
                for image_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = pdf.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_path = (
                        self.path[:-4]
                        + f".page{page_number + 1:03d}"
                        + f".img{image_index + 1:02d}"
                        + ".png"
                    )
                    with open(image_path, "wb") as image_file:
                        image_file.write(image_bytes)
                    log.info(f"Wrote {File(image_path)}")
