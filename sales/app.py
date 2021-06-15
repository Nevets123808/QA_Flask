from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:flipit@35.197.228.206:3306/sales"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    purchases = db.relationship("Sales", backref = "buyer")

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    orders = db.relationship("Sales", backref = "item")

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    
