from enum import Enum
from typing import List, Optional, Union

import strawberry

from bookstore.core.infrastructure.graphql.types import Success, Failure, Entity


@strawberry.input
class AuthorInput:
    first_name: str
    last_name: str


@strawberry.type
class Author:
    first_name: str
    last_name: str


@strawberry.enum
class BookCoverType(Enum):
    PAPER_BACK = "paper-back"
    HARD_COVER = "hard-cover"


@strawberry.type
class BookType:
    number_of_pages: int
    cover_type: BookCoverType


@strawberry.type
class VideoMedia:
    length: str


@strawberry.type
class Resource(Entity):
    title: str
    author: List[Author]
    quantity: Optional[int] = 1
    media_type: Union[BookType, VideoMedia] | None = None


@strawberry.type
class BookSuccess(Success):
    data: Resource


@strawberry.type
class BookFailure(Failure):
    model = Resource
