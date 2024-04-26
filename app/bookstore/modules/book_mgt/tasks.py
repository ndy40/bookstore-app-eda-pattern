from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.celery import app
from bookstore.core.infrastructure.publisher import publish
from bookstore.modules.book_mgt import services
from bookstore.modules.book_mgt.commands import ReserveBook
from bookstore.modules.book_mgt.events import BookCreated

_logger = get_task_logger(__name__)


@app.task(name="command.createbook")
def create_new_book(
    msg: "CreateBook",
):

    _logger.debug("creating new book")
    book = services.create_new_book(
        title=msg.title,
        author_first_name=msg.author_first_name,
        author_last_name=msg.author_last_name,
        dob=msg.dob,
    )

    # publish event
    event = BookCreated(book_id=book.id, title=book.title, author=book.author)
    reserve_book = ReserveBook(book_id=book.id, title=book.title)
    publish(event, reserve_book)


@app.task(name="event.bookcreated")
def handle_book_created_event(msg: "BookCreated"):
    _logger.info("handling book created event")
