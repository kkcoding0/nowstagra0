#-*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)

from nowstagram import views,models