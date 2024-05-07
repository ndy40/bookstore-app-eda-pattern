from typing import Optional, List

from bookstore.core.domain.value_objects import Command, EntityUUID
from bookstore.modules.book_mgt.value_objects import Author


class CreateBook(Command):
    title: str
    author: List[Author]


class UpdateBook(Command):
    author_first_name: Optional[str] = None
    author_last_name: Optional[str] = None


class ReserveBook(Command):
    book_id: EntityUUID
    title: str
