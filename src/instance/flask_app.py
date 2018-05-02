# instance/flask_app.py

# third-party imports
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

# local imports
from src.instance.config import config
import src.misc.constants as cn
from src.misc.service_logger import serviceLogger as logger
from src.core.db_connection import DataBase

# flask application initialization
app = Flask(__name__)

# cross origin resource sharing
CORS(app)

# database connection
try:
    connection = DataBase().get()
except Exception as ex:
    logger.error(cn.DB_UNAVAILABLE, exc_info=True)
    print("Database unavailable")
    connection = None

# restplus swagger-ui
api = Api(app, version='1.0', title='flask-minimal-boilerplate', prefix='/api/v1',
          description='A boilerplate for flask-restful API services')

# Flask app configurations
app.config['SQLALCHEMY_BINDS'] = {
                                    'bind_db': config['database']['db_url']
                                 }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

# SQLAlchemy instantiation
db = SQLAlchemy(app)
db.create_all(bind=['bind_db'])
db.create_all()

