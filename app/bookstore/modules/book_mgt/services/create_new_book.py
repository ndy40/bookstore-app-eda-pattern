from bookstore.core.infrastructure.database.connect import client
from bookstore.core.infrastructure.database.models import BookType
from bookstore.modules.book_mgt.domain import Author, Book
from bookstore.modules.book_mgt.repository import BookRepository, book_repo
from bookstore.modules.book_mgt.value_objects import BookType as BookTypeValue


def create_new_book(
        title: str,
        author_first_name: str,
        author_last_name: str,
        quantity: int = 1,
        media_type: BookTypeValue = None,
) -> Book:
    book = Book(
        title=title,
        authors=[
            Author(
                first_name=author_first_name,
                last_name=author_last_name,
            )
        ],
        quantity=quantity,
        media_type=BookType(
            number_of_pages=media_type.number_of_pages,
            cover_type=media_type.cover_type.value,
        ),
    )
    book_repo.persist(book)
    return book


def get_books():
    repo = BookRepository(client=client)
    return repo.all()
