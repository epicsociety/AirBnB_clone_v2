#!/usr/bin/python3
"""This module instantiates an object of class file_storage
if the env var is HBNB_TYPE_STORAGE it will instantiates
DBStorage
else, it will instantiates FileStorage
"""


from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

hbnb_type_storage = getenv('HBNB_TYPE_STORAGE')

if hbnb_type_storage == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
