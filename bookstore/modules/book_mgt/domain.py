import dataclasses

from bookstore.modules.book_mgt.value_objects import Author
from bookstore.core.domain.models import AggregateRoot


@dataclasses.dataclass(kw_only=True)
class Book(AggregateRoot):
    title: str
    author: Author

