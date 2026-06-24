import os
from functools import cached_property

from utils_future import File


class TableImageMixin:
    @cached_property
    def dir_original_images(self) -> str:
        return os.path.join(self.dir_data, "original.images")

    def get_image_files(self):
        if not os.path.exists(self.dir_original_images):
            return []
        image_files = []
        for file_name in os.listdir(self.dir_original_images):
            if file_name.endswith(".png"):
                image_file = File(os.path.join(self.dir_data, file_name))
                image_files.append(image_file)
        image_files.sort(key=lambda f: f.path)
        return image_files

    @property
    def first_image_file(self):
        image_files = self.get_image_files()
        if not image_files:
            return None
        return image_files[0]

    def build_images(self, force=False):
        if (
            self.first_image_file
            and self.first_image_file.exists
            and not force
        ):
            return

        self.pdf_file.extract_images()
