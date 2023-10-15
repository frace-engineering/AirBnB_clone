from models.engine.file_storage import FileStorage

import os


def resetStorage():
    """Resets the storage"""

    FileStorage_FileStorage__objects = {}
    if os.path.isfile(FileStorage._FileStorage__file_path):
        os.remove(FileStorage._FileStorage__file_path)
