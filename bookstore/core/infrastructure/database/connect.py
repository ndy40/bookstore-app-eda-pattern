from pymongo import MongoClient

from bookstore.core.infrastructure.config import config

client = MongoClient(config.DB_URL)

