from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.bus.events import event_bus
from bookstore.core.infrastructure.celery import app

_logger = get_task_logger(__name__)


@event_bus.on("BookCreated")
@app.task
def update_available_book_data(msg: "BookCreated"):
    _logger.info("Updating book availability records")
