# namespaces

from src.instance.flask_app import api

user_api = api.namespace('users', description='operations related to Users')
prod_api = api.namespace('products', description='operations related to Products')
