from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from typing import List
from .objects import Category, Activity
from .stores import TimesureStore


class BaseManager:
    def __init__(self, store: TimesureStore):
        self.store = store


    def session(self):
        return Session(self.store.engine)


class CategoryManager(BaseManager):
    def __init__(self, store: TimesureStore):
        super().__init__(store)


    def add(self, c: Category):
        with self.session() as session:
            session.add(c)
            session.commit()


    def get_all(self) -> List[Category]:
        stmt = select(Category)
        
        with Session(self.store.engine) as session:
            for row in session.scalars(stmt):
                yield row


class ActivityManager:
    def __init__(self, store: TimesureStore):
        self.store = store

    

    def get_all(self) -> List[Activity]:
        stmt = select(Activity)
        
        with Session(self.store.engine) as session:
            for row in session.scalars(stmt):
                yield row