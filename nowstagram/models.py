#-*-coding:utf-8-*-
from nowstagram import db
import random
from datetime import datetime

class Image(db.Model):
    id = db.column(db.Integer,primary_key=True,autoincrement=True)
    url = db.column(db.String(512))
    user_id = db.column(db.Integer,db.ForeignKey('user.id'))
    created_date = db.column(db.DateTime)

    def __init__(self,url,user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime

    def __repr__(self):
        return ('<Image %d %s>'%(self.id,self.url))

class User(db.Model):
    __tablename__ = 'myuser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image')
    # images = db.relationship('Image', backref='user', lazy='dynamic')
    #images = db.relationship('Image')

    def __init__(self, username, password):
        self.username = username
        self.password = password #暂时明文，下节课讲解加密
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 't.png'

    def __repr__(self):
        return ('<User %d %s>'%(self.id,self.username))
