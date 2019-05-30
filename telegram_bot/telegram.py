## 텔레그램 챗봇(Chat Bot) 만들기

# 라이브러리 import
import requests
import random

# 텔레그램 챗봇 토큰값
token = config('TELEGRAM_TOKEN')

# API url 주소값
api_url = f'https://api.telegram.org/bot{token}'

# 텔레그램 본인 ID값
chat_id = config('TELEGRAM_ID')

# 챗봇에게 보낼 메시지
# text = input('메시지를 입력하세요:')
text = random.sample(range(1, 46), 6)


response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')