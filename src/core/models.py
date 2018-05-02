from src.instance.flask_app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self,username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '{"User":"%s","Email":"%s"}' % (self.username, self.email)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), unique=True)
    product_type = db.Column(db.String(10))

    def __init__(self,product_name, product_type):
        self.product_name = product_name
        self.product_type = product_type

    def __repr__(self):
        return '{"Product":"%s","Type":"%s"}' % (self.product_name, self.product_type)
