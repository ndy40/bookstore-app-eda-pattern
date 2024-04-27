import dataclasses
from typing import Annotated

from pydantic import AfterValidator

from bookstore.core.domain.models import AggregateRoot
from bookstore.modules.book_mgt.value_objects import Author

supported_media_types = ["paperback", "audio", "video", "podcast", "film"]

MediaType = Annotated[str, AfterValidator(lambda x: x in supported_media_types)]


@dataclasses.dataclass(kw_only=True)
class Book(AggregateRoot):
    title: str
    author: Author
    quantity: int | None = 1
    media_type: MediaType | None = None
    volume: str | None = None
