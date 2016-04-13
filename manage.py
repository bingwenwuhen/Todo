__author__ = 'xiaxuan'
from flask_script import Manager
from app import app
from app import models
from app import sdb

manager = Manager(app)


@manager.command
def save():
    user = models.User(1, 'xiaxuan')
    sdb.session.add(user)
    sdb.session.commit()


@manager.command
def query_all():
    list = models.User.query.all()
    for u in list:
        print str(u.id) + " " + u.name


if __name__ == "__main__":
    manager.run()
