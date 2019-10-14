from app import db
from sqlalchemy_utils import generic_relationship


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password


class Documents(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {'extend_existing': True}

    doc_id = db.Column(db.Integer, primary_key=True)
    marksheet_10th = db.Column(db.String)
    marksheet_12th = db.Column(db.String)
    marksheet_bsc = db.Column(db.String)
    marksheet_msc = db.Column(db.String)
    object_type = db.Column(db.Unicode(255))
    object_id = db.Column(db.Integer)
    object = generic_relationship(object_type, object_id)


db.create_all()
