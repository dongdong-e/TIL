## 라이브러리 import
from flask import Flask, render_template, request
import requests
import random
from decouple import config


## Flask 설정
app = Flask(__name__)


# 텔레그램 챗봇 값
token = config('TELEGRAM_TOKEN')
# API url 주소값
api_url = f'https://api.telegram.org/bot{token}'

# 네이버 파파코 값
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
papago_url = 'https://openapi.naver.com/v1/papago/n2mt'


## 웹페이지 만들기
# 프론트 페이지
@app.route(f'/{token}', methods = ['POST'])
def telegram():
    # return '', 200   # '': 응답을 받을 메시지 / 200: 응답코드(Status Code)
    # print(request.get_json())

    # 딕셔너리에서 key값 가져오는 방법
    # 1. lotto['key'] => value, 'key'가 없다면 에러 발생!
    # 2. lotto.get('key') => value, 'key'가 없다면 None 리턴!

    message = request.get_json().get('message')

    ## data 가져오기
    if message is not None:
        # 보낸 사람 id
        chat_id = message.get('from').get('id')
        # 보낸 사람에게 받은 메시지
        text = message.get('text')

        # 1. 로또
        if '로또' in text:
        # 보낸 사람에게 다시 메시지 보내기
            text = random.sample(range(1, 46), 6)


        # 2. 네이버 번역
        # /번역 안녕하세요!
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
            }

            # 요청 변수 설정
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:]
            }

            papago_res = requests.post(papago_url, headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')

        send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

        # sendMessage 요청 보내기
        response = requests.get(send_url)



    return '', 200   # '': 응답을 받을 메시지 / 200: 응답코드(Status Code)


if __name__ == '__main__':
    app.run(debug=True)