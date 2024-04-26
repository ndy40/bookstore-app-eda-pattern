from datetime import date

from bookstore.core.infrastructure.database.connect import client
from bookstore.modules.book_mgt.domain import Author
from bookstore.modules.book_mgt.domain import Book
from bookstore.modules.book_mgt.repository import BookRepository
from bookstore.modules.book_mgt.value_objects import Name


def create_new_book(
    title: str, author_first_name: str, author_last_name: str, dob: date = None
) -> Book:

    book = Book(
        title=title,
        author=Author(
            first_name=Name(author_first_name),
            last_name=Name(author_last_name),
            dob=dob,
        ),
    )
    repo = BookRepository(client=client)
    repo.persist(book)
    return book
