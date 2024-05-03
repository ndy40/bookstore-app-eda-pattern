from datetime import datetime
from typing import Optional

from bunnet import Document
from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[datetime] = None


class Book(Document):
    title: str
    author: Author
    quantity: int
    media_type: str | None = None
    quantity: int | None = None
    volume: str | None = None

    class Settings:
        keep_nulls = False
