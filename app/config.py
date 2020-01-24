import os


class Config:
    DB_NAME = os.getenv('DB_NAME', 'todolists')
    DB_PORT = os.getenv('DB_PORT', '27017')
    DB_URL = os.getenv('DB_URL', 'localhost')
    MONGO_URI = f'mongodb://{DB_URL}:{DB_PORT}/{DB_NAME}'
