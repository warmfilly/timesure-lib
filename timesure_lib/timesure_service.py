import sqlite3
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from typing import List

from .objects import TimesureBase, Category

class CategoryManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = self.get_engine()

    
    def get_engine(self):
        return create_engine('sqlite:///' + self.db_path)


    def get_all(self) -> List[Category]:
        stmt = select(Category)
        
        with Session(self.engine) as session:
            for row in session.scalars(stmt):
                yield row



class TimesureService:
    def __init__(self, db_path: str):
        self.db_path = db_path

        self.categories = CategoryManager(self.db_path)


    def close(self):
        self.connection.close()

    def _get_engine(self):
        return sqlalchemy.create_engine('sqlite:///' + self.db_path)
        

    def _get_metadata(self):
        m = TimesureBase.metadata

        m.create_all(self.engine)

        return m

    
