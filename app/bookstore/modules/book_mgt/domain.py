import dataclasses

from bookstore.core.domain.models import AggregateRoot
from bookstore.modules.book_mgt.value_objects import Author


@dataclasses.dataclass(kw_only=True)
class Book(AggregateRoot):
    title: str
    author: Author
