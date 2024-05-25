from flask import Flask
import random

app = Flask(__name__)

list_items = [] # 아이템을 저장하기 위한 목록

@app.route('/')
def index():
    # 목록이 조회되는 화면
    return "index"

@app.route('/read/<int:id>')
def read(id):
    # 아이템을 조회되는 화면
    return "read: " + str(id)

@app.route('/create')
def create():
    # 아이템을 생성하는 화면
    return "create"

app.run(port=8000, debug=True)