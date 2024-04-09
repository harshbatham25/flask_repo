from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Customer is the name of our table
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50),nullable=False, unique = True)
