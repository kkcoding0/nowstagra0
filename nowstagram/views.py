#-*-coding:utf-8-*-
from nowstagram import app

@app.route('/')
def index():
    return 'hello'