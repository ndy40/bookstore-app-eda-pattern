from celery.utils.log import get_task_logger

from bookstore.core.infrastructure.bus.commands import CommandHandler, TCommand
from bookstore.core.infrastructure.celery import app
from bookstore.modules.book_mgt.commands import CreateBook
from bookstore.modules.book_mgt.events import BookCreated

_logger = get_task_logger(__name__)


# @app.task()
# def create_new_book(
#     msg: "CreateBook",
# ):
#
#     _logger.info("creating new book")
#     book = services.create_new_book(
#         title=msg.title,
#         author_first_name=msg.author[0].first_name,
#         author_last_name=msg.author[0].last_name,
#     )
#     _logger.info(f"New book crated {book.id}")
#     return BookCreated(book_id=book.id, title=book.title, author=book.author)


class CreateTask(CommandHandler[CreateBook], app.Task):

    def handle(self, command: TCommand) -> None:

        pass

    def run(self, cmd: CreateBook):
        _logger.info(f"Tasks fetched")
        self.handle(cmd)


@app.task(name="handle_book_created_event")
def handle_book_created_event(msg: "BookCreated"):
    _logger.info("handling book created event")


app.task.register(CreateTask)
