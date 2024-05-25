from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/random')
def rand(): # 함수 명 random 지정 시 random 모듈과 동일한 이름을 가지므로 에러가 발생
    random_color = "#%06x" % random.randint(0, 0xFFFFFF)
    return "Random: " + \
        "<strong style='color: "+random_color+";'>" + \
            str(random.random()) + \
        "</strong>"

@app.route('/hello')
def hello():
    return 'Hello Flask'

@app.route('/read/<int:id>') 
def read(id): # 라우팅 경로에 id 위치의 값을 받기 위해 동일한 이름의 id 인자값을 설정
    return 'Read: ' + str(id) # int형 인자 이므로, 문자열 형변환을 수행

app.run(port=8000, debug=True)