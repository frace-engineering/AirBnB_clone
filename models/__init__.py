#!/usr/bin/python3
"""__init__ module for the model package"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()