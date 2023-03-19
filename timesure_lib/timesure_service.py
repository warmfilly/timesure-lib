from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer
from typing import List

from .objects import TimesureBaseObject, Category
from .managers import CategoryManager
from .stores import TimesureStore



# TimesureService needs a store member or at least an engine so it can initialize the db
class TimesureService():
    def __init__(self, db_path: str):
        self.store = TimesureStore(db_path)

        self.categories = CategoryManager(self.store)
        #self.activities = ActivityManager(db_path)

    def initialize_db(self):
        TimesureBaseObject.metadata.create_all(self.store.engine)

