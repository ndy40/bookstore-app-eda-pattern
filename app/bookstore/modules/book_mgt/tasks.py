from celery.utils.log import get_task_logger

from bookstore.core.domain.constants import EventRegistry
from bookstore.core.infrastructure.bus import event_bus
from bookstore.core.infrastructure.celery import app
from bookstore.core.infrastructure.publisher import publish
from bookstore.modules.book_mgt import services
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
    publish(event)
    return book


@event_bus.on(EventRegistry.BOOK_CREATED)
@app.task(name="handle_book_created_event")
def handle_book_created_event(msg: "BookCreated"):
    _logger.info("handling book created event")
