from datetime import date

import strawberry


@strawberry.type
class Author:
    first_name: str
    last_name: str
    dob: date | None = None


@strawberry.type
class Book:
    title: str
    author: Author
