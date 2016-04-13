__author__ = 'xiaxuan'
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = MongoEngine(app)
sdb = SQLAlchemy(app)

from app import models
from app import views

