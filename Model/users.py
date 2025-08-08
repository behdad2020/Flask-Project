from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    fullName = db.Column(db.String(50) , nullable = False)
    email = db.Column(db.String(50) , unique = True , nullable = False)
    phone = db.Column(db.String(50) , unique = True , nullable = False)
    password = db.Column(db.String(50) , nullable = False)
    userType = db.Column(db.String(50) , nullable = False)
    country = db.Column(db.String(50) , nullable = False)
    university = db.Column(db.String(50) , nullable = False)
    fieldOfStudy = db.Column(db.String(50) , nullable = False)
    passportNumber = db.Column(db.String(50) , nullable = False)