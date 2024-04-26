from pydantic import ConfigDict

from bookstore.core.domain.models import EntityId
from bookstore.core.domain.value_objects import Event
from bookstore.modules.book_mgt.value_objects import Author


class BookCreated(Event):
    book_id: EntityId
    title: str
    author: Author

    model_config = ConfigDict(arbitrary_types_allowed=True)
