import os

from utils_future import JSONFile


class TableMetadataMixin:
    METADATA_FILE = JSONFile(os.path.join('data', 'table_metadata.json'))

    @classmethod
    def load_metadata(cls):
        return cls.METADATA_FILE.read()
