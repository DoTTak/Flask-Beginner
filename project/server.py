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

app.run(port=8000, debug=True)