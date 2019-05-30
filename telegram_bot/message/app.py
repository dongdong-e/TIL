## 라이브러리 import
from flask import Flask, render_template, request
import requests
import random

## Flask 설정
app = Flask(__name__)


## 웹페이지 만들기
# 메시지 입력 페이지 만들기
@app.route('/write')
def write():
    return render_template('write.html')


# 메시지 전송 완료 페이지 만들기
@app.route('/send')
def send():
    # 텔레그램 챗봇 토큰값
    token = '816801571:AAFoEQdcaF-4nsWjq4Y4acQP0ilvgassfsM'

    # API url 주소값
    api_url = f'https://api.telegram.org/bot{token}'

    # 텔레그램 본인 ID값
    chat_id = '784197368'

    # 챗봇에게 보낼 메시지
    # text = input('메시지를 입력하세요:')
    # text = random.sample(range(1, 46), 6)
    text = request.args.get('message')

    response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

    return 'Complete'



if __name__ == '__main__':
    app.run(debug=True)