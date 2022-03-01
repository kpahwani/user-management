import os


class BaseConfig(object):
    MONGO_DB_CONNECTION_HOST = os.environ.get("MONGO_DB_CONNECTION_HOST", "localhost")
    MONGO_DB_CONNECTION_PORT = os.environ.get("MONGO_DB_CONNECTION_HOST", "27017")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "users")
