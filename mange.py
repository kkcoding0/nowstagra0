#-*-coding:utf-8-*-
from nowstagram import app,db
from nowstagram.models import User,Image
from flask_script import Manager
import random

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(100):
        db.session.add(User('yonghu'+str(i),'a'+str(i)))

    db.session.commit()


if __name__ == '__main__':
    manager.run()
