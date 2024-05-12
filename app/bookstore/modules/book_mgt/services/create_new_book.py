from bookstore.core.infrastructure.database.connect import client
from bookstore.modules.book_mgt.domain import Author, Book
from bookstore.modules.book_mgt.repository import BookRepository, book_repo


def create_new_book(title: str, author_first_name: str, author_last_name: str) -> Book:

    book = Book(
        title=title,
        author=[
            Author(
                first_name=author_first_name,
                last_name=author_last_name,
            )
        ],
        quantity=1,
    )
    book_repo.persist(book)
    return book


def get_books():
    repo = BookRepository(client=client)
    return repo.all()
