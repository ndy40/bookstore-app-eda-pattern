from bunnet import Document
from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str


class Book(Document):
    title: str
    author: Author
