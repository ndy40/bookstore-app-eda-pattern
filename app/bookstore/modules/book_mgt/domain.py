import dataclasses
from typing import List, Optional

from bookstore.core.domain.models import AggregateRoot
from bookstore.modules.book_mgt.value_objects import Author, BookType

supported_media_types = ["paperback", "audio", "video", "podcast", "film"]


@dataclasses.dataclass(kw_only=True)
class Book(AggregateRoot):
    title: str
    authors: List[Author]
    quantity: int | None = 1
    media_type: Optional[BookType] = None
    volume: str | None = None
