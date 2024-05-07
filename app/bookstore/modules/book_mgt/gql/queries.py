from typing import List

import strawberry
from strawberry.tools import merge_types

from . import resolvers
from .types import Resource


@strawberry.type
class BookQuery:
    books: List[Resource] = strawberry.field(name="books", resolver=resolvers.get_books)


BookMgtQuery = merge_types("BookMgtQuery", (BookQuery,))
