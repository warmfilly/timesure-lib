from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class TimesureBase(DeclarativeBase):
    pass


class Category(TimesureBase):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    creation_time: Mapped[int]

    def __repr__(self):
        return f'{self.id}|{self.name}|{self.description}|{self.creation_time}'


