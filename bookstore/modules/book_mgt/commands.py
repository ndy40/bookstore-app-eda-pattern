import dataclasses

from bookstore.core.domain.value_objects import Command


@dataclasses.dataclass
class Author:
    first_name: str | None = None
    last_name: str | None = None


class CreateBook(Command):
    title: str
    author: Author


class UpdateBook(Command):
    author: Author | None = None

