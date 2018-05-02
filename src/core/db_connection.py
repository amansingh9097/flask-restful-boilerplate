import psycopg2
from src.instance.config import config
from psycopg2.extras import RealDictCursor


class DataBase():
    def __init__(self):
        self.connection = psycopg2.connect(config['database']['db_url'])

    def get(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)