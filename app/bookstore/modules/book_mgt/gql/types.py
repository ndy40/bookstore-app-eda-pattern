from enum import Enum
from typing import List, Optional

import strawberry

from bookstore.core.infrastructure.graphql.types import Success, Failure, Entity


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
    authors: List[Author]
    quantity: Optional[int] = 1
    media_type: BookType | None = None


@strawberry.type
class BookSuccess(Success):
    data: Resource


@strawberry.type
class BookFailure(Failure):
    model = Resource


@strawberry.input
class AuthorInput:
    first_name: str
    last_name: str

@strawberry.input
class VideoMediaInput:
    length: str


@strawberry.input
class MediaInputType:
    number_of_pages: int
    cover_type: BookCoverType
