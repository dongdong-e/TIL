from flask import Flask, render_template
import random
app = Flask(__name__)

# 1. FLASK_APP=hello.py flask run
# 코드를 수정할 때마다 수동으로 서버 on/off를 해야하는 코드

# 2. FLASK_DEBUG=1 FLASK_APP=hello.py flask run
# 서버를 항상 끄고 켜야하는 불편함을 해결하기 위해 사용하는 코드

# 3. python hello.py
# __name__ == '__main__' 함수를 사용하여 더 간결하게 서버를 관리하는 코드
# if __name__ == '__main__':
#     app.run(debug=True)


# @ (골뱅이): 함수에서 다른 함수의 결과값을 불러올 때 사용
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/mulcam')
def mulcam():
    return 'This is Multicampus!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다. {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{result}'

# <int:people>
# random.sample: 리스트 안에서 랜덤으로 추출
@app.route('/lunch/<int:people>')
def lunch(people):

    menu = ['피자', '치킨', '햄버거', '라면', '짜장면', '빵', '토스트']

    # return f'{random.sample(menu, people)}'
    return str(random.sample(menu, people))

@app.route('/html')
def html():
    multiple_string = """
        <h1>This is h1 tag</h1>
        <p>This is p tag</p>
    """
    return multiple_string

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')


# Template Variable 사용하기
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name = name)

@app.route('/menu_list')
def menu_list():
    menu = ['피자', '치킨', '햄버거', '라면', '짜장면', '빵', '토스트']

    return render_template('menu_list.html', menu_list = menu)



if __name__ == '__main__':
    app.run(debug=True)