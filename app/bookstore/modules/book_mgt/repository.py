from bookstore.core.infrastructure.data_mapper import DataMapper
from bookstore.core.infrastructure.repository import EntityRepository
from bookstore.modules.book_mgt.domain import Book
from bookstore.modules.book_mgt.models import Author
from .models import Book as BookModel


class BookDataMapper(DataMapper[Book, BookModel]):
    def map_from_entity_to_model(self, entity: Book) -> BookModel:
        return BookModel(
            id=entity.id,
            title=entity.title,
            author=Author(
                first_name=entity.author.first_name, last_name=entity.author.last_name
            ),
        )

    def map_from_model_to_entity(self, instance: BookModel) -> Book:
        return Book(
            id=instance.id,
            title=instance.title,
            author=Author(
                first_name=instance.author.first_name,
                last_name=instance.author.last_name,
            ),
        )


class BookRepository(EntityRepository):
    mapper_class = BookDataMapper
    model_class = BookModel
