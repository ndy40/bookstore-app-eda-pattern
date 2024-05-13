from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.bus.commands import command_bus
from bookstore.core.infrastructure.bus.events import event_bus
from bookstore.core.infrastructure.celery import app
from bookstore.modules.book_mgt import services
from bookstore.modules.book_mgt.commands import CreateBook
from bookstore.modules.book_mgt.events import BookCreated

_logger = get_task_logger(__name__)


@app.task()
def create_new_book(
        msg: CreateBook,
):
    _logger.info("creating new book")
    book = services.create_new_book(
        title=msg.title,
        author_first_name=msg.author[0].first_name,
        author_last_name=msg.author[0].last_name,
        media_type=msg.media_type,
        quantity=msg.quantity
    )
    _logger.info(f"New book crated {book.id}")

    print(book.__dict__)

    media_type = None

    if media_type := book.media_type:
        media_type = BookType(
            number_of_pages=book.media_type.number_of_pages,
            cover_type=book.media_type.cover_type.value,
        )

    return BookCreated(
        book_id=book.id,
        title=book.title,
        author=book.authors,
        quantity=book.quantity,
        media_type=media_type,
    )


@event_bus.on("BookCreated")
@app.task(name="handle_book_created_event")
def handle_book_created_event(msg: "BookCreated"):
    _logger.info("handling book created event")


command_bus.register(handler=create_new_book)
