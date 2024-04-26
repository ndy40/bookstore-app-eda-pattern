import dataclasses
import datetime
from typing import Optional

from bookstore.core.domain.value_objects import Command, EntityUUID


@dataclasses.dataclass
class Author:
    first_name: str | None = None
    last_name: str | None = None


class CreateBook(Command):
    title: str
    author_first_name: str
    author_last_name: str
    dob: Optional[datetime.date] = None


class UpdateBook(Command):
    author_first_name: Optional[str] = None
    author_last_name: Optional[str] = None
    author_dob: Optional[datetime.datetime] = None


class ReserveBook(Command):
    book_id: EntityUUID
    title: str
