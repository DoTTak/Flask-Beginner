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
        <button type="botton" onclick="location.href='/create'">create</button>
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

    # 수정, 삭제 버튼
    menu = f"""
    <p>
    <button type="botton" onclick="location.href='/edit/{id}'">edit</button>
    <button type="botton" onclick="location.href='/delete/{id}'">delete</button>
    </p>
    """

    return template(getItems(), f"""<hr><h2>Title: {title}</h2>{menu}{content}""")

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

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    if request.method == 'GET':
        # 선택된 아이템을 조회
        now_item = {}
        for item in list_items:
            if id == item['id']:
                now_item = item
                break

        # 아이템 수정을 위한 html 코드
        html = f"""
        <h2>Edit</h2>
        <form action="/edit/{now_item['id']}" method="POST">
            <p>title: <input type="text" name="title" placeholder="title" value="{now_item['title']}"></input></p>
            <p><textarea name="content" placeholder="content" >{now_item['content']}</textarea></p>
            <input type="submit" value="edit">
        </form>
        """
        return template(getItems(), f"<hr>{html}")
    else:
        # 일치하는 아이템의 경우 제목과 콘텐츠를 변경
        for item in list_items:
            if id == item['id']:
                item['title'] = request.form['title']
                item['content'] = request.form['content']
                break
        # 수정 완료 시 수정된 아이템의 정보로 이동
        return redirect(f"/read/{id}")

@app.route('/delete/<int:id>')
def delete(id):

    # 일치하는 id 값이 있을 경우 목록에서 제거
    for item in list_items:
        if id == item['id']:
            list_items.remove(item)
            break

    # 삭제 시 조회 페이지로 이동
    return redirect("/")


app.run(port=8000, debug=True)