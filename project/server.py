from flask import Flask
from flask import request, redirect
import random

app = Flask(__name__)

nextId = 4 # 다음에 추가될 아이템 번호
list_items = [ # 아이템을 저장하기 위한 목록
    {"id": 1, "title": "html", "content": "html is ..."},
    {"id": 2, "title": "javascript", "content": "javascript is ..."},
    {"id": 3, "title": "css", "content": "css is ..."}
]

def template(contents, content):
    # 응답할 html 코드
    html = f'''
    <html>
    <body>
        <h1>List</h1>
        <ol>
            {contents}
        </ol>
        {content}
    </body>
    </html>
    '''

    return html

def getItems():
    # html 응답 코드 내 목록을 조회하기 위한 구현부
    li_tags = ''
    for item in list_items:
        li_tags += f'<li><a href="/read/{item["id"]}">{item["title"]}</a></li>'
    
    return li_tags

@app.route('/')
def index():
    # 목록이 조회되는 화면
    return template(getItems(), "")

@app.route('/read/<int:id>')
def read(id):
    # 아이템을 조회되는 화면
    
    # 선택한 아이템에 대한 제목과 콘텐츠를 담기 위한 구현부
    title = '' # 제목을 저장할 변수
    content = '' # 콘텐츠를 저장할 변수
    for item in list_items:
        # 목록을 순회할 때 선택한 아이템의 경우 제목과 콘텐츠를 변수에 저장
        if id == item['id']:
            title = item["title"]
            content = item["content"]
            break
    
    return template(getItems(), f"""<hr><h2>Title: {title}</h2>{content}""")

@app.route('/create', methods=['GET', 'POST'])
def create():
    # 아이템을 생성하는 화면

    # GET 요청을 수행하는 로직
    if request.method == 'GET':

        # 아이템 생성을 위한 html 코드
        html = """
        <form action="/create" method="POST">
            <p>title: <input type="text" name="title" placeholder="title"></input></p>
            <p><textarea name="content" placeholder="content"></textarea></p>
            <input type="submit" value="create">
        </form>
        """
        return template(getItems(), f"<hr>{html}")
    
    # POST 요청을 수행하는 로직
    else:
        global nextId # 지역변수로 인식되지 않기 위함
        title = request.form['title'] # 클라이언트로 부터 HTTP Request 데이터 'title' 을 받음
        content = request.form['content'] # 클라이언트로 부터 HTTP Request 데이터 'content' 을 받음
        # 새로운 아이템 생성
        new_item = {"id": nextId, "title": title, "content": content}
        # 목록에 새로운 아이템을 삽입
        list_items.append(new_item)
        # 생성한 아이템의 번호 저장
        now_id = nextId
        # 다음 아이템을 위한 아이템 번호 증가시키기
        nextId = nextId + 1

        return redirect("/read/" + str(now_id))

app.run(port=8000, debug=True)