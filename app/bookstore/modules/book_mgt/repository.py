from bookstore.core.infrastructure.data_mapper import DataMapper
from bookstore.core.infrastructure.database.connect import client
from bookstore.core.infrastructure.database.models import Book as BookModel, Author, BookType as BookTypeModel
from bookstore.core.infrastructure.database.repository import EntityRepository
from bookstore.modules.book_mgt import domain
from bookstore.modules.book_mgt.value_objects import BookType


class _BookDataMapper(DataMapper[domain.Book, BookModel]):
    def map_from_entity_to_model(self, entity: domain.Book) -> BookModel:
        authors = [
            Author(
                first_name=author.first_name,
                last_name=author.last_name,
            )
            for author in entity.authors
        ]

        media_type = None

        if entity.media_type:
            media_type = BookTypeModel(
                number_of_pages=entity.media_type.number_of_pages,
                cover_type=entity.media_type.cover_type.value,
            )
        return BookModel(
            id=entity.id,
            title=entity.title,
            authors=authors,
            quantity=entity.quantity,
            media_type=media_type,
        )

    def map_from_model_to_entity(self, instance: BookModel) -> domain.Book:
        media_type = None

        if instance.media_type:
            media_type = BookType(number_of_pages=instance.media_type.number_of_pages,
                                  cover_type=instance.media_type.cover_type.value)

        return domain.Book(
            id=instance.id,
            title=instance.title,
            authors=[domain.Author(
                first_name=author.first_name,
                last_name=author.last_name,
            ) for author in instance.authors],
            quantity=instance.quantity,
            volume=instance.volume,
            media_type=media_type
        )


class BookRepository(EntityRepository):
    mapper_class = _BookDataMapper
    model_class = BookModel
    active_model = BookModel


#  instances of Repositories

book_repo = BookRepository(client=client)
