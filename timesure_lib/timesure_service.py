import sqlite3
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from typing import List

from .objects import TimesureBase, Category
from .managers import CategoryManager

class TimesureService:
    def __init__(self, db_path: str):
        store = TimesureStore(db_path)

        self.categories = store.categories


class TimesureStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = create_engine('sqlite:///' + db_path)
        

        self.categories = CategoryManager(self)

    
    # def get_session(self):
    #     return Session(self.enmgi


    
class CategoryManager:
    def __init__(self, store: TimesureStore):
        self.store = store

    
    def get_all(self) -> List[Category]:
        stmt = select(Category)

        with Session(self.store.engine) as session:
            for category in session.scalars(stmt):
                yield category

