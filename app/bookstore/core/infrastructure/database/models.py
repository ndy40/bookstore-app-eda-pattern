from enum import Enum
from typing import List

from bunnet import Document
from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str


class BookCoverType(Enum):
    PAPER_BACK = "paper-back"
    HARD_COVER = "hard-cover"


class BookType(BaseModel):
    number_of_pages: int
    cover_type: BookCoverType


class Book(Document):
    title: str
    author: List[Author]
    quantity: int
    media_type: BookType | None = None
    quantity: int | None = None
    volume: str | None = None

    class Settings:
        keep_nulls = False
