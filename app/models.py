__author__ = 'xiaxuan'
import datetime
from app import db
from app import sdb


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

    def to_json(self):
        return {
            'id': str(self.id),
            'content': self.content,
            'time': self.time,
            'status': self.status
        }


class User(sdb.Model):
    id = sdb.Column(sdb.Integer, primary_key=True)
    name = sdb.Column(sdb.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name
