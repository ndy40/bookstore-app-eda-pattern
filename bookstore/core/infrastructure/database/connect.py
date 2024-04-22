from pymongo import MongoClient

from bookstore.core.infrastructure.config import config

client: MongoClient = MongoClient(config.DB_URL)

