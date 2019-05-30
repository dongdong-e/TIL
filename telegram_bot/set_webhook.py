## 라이브러리 import
import requests
from decouple import config
from flask import Flask

## 텔레그램 챗봇 토큰값
token = config('TELEGRAM_TOKEN')

## API url 주소값
api_url = f'https://api.telegram.org/bot{token}'

## flask_url + SetWebhook
flask_url = f'https://kyd9800.pythonanywhere.com/{token}'
set_url = f'{api_url}/setWebhook?url={flask_url}'

response = requests.get(set_url)
print(response.text)