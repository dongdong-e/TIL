# 라이브러리 불러오기
from django.shortcuts import render
import random
from datetime import datetime
import json
import requests

# Create your views here.
# request는 필수요소!
# html 이름은 함수와 동일하게 만듦
def index(request):
    return render(request, 'pages/index.html')


def hola(request):
    return render(request, 'pages/hola.html')


# 통상적으로 context를 사용한다.
def dinner(request):
    menu = ['짜장면', '샐러드', '햄버거', '스파게티', '치킨']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)


def introduce(request, name, age):
    context = {'name': name,
               'age': age}
    return render(request, 'pages/introduce.html', context)


def times(request, num1, num2):
    context = {'num1': num1,
               'num2': num2,
               'result': num1 * num2}
    return render(request, 'pages/times.html', context)


def area(request, num1):
    num2 = 3.14
    context = {'num1': num1,
               'result': num1**2 * num2}
    return render(request, 'pages/area.html', context)


def template_language(request):
    menus = ['짜장면', '샐러드', '햄버거', '스파게티', '치킨']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = ['김영동', 'KYD']
    datetimenow = datetime.now()
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)


def birth_day(request):
    today = datetime.today().strftime('%m-%d')

    birth_date = '09-02'

    if today == birth_date:
        context = {'result': '생일 축하합니다.'}
    else:
        context = {'result': '오늘은 생일이 아니군요.'}

    return render(request, 'pages/birth_day.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    message_01 = request.GET.get('message_01')
    message_02 = request.GET.get('message_02')
    context = {'message_01': message_01,
               'message_02': message_02}
    return render(request, 'pages/catch.html', context)


def lotto(request):
    return render(request, 'pages/lotto.html')


def lotto_number(request):
    if '로또' in request.GET.get('message'):
        lotto_number = sorted(random.sample(range(1, 46), 6))
        context = {'lotto_number': lotto_number}
    return render(request, 'pages/lotto_number.html', context)


def lotto_01(request):
    return render(request, 'pages/lotto_01.html')


def get(request):
    lottos = range(1, 46)
    pick = sorted(random.sample(lottos, 6))
    name = request.GET.get('name')
    context = {'pick': pick, 'name': name}
    return render(request, 'pages/get.html', context)


def lotto_02(request):
    return render(request, 'pages/lotto_02.html')


def pick_lotto(request):
    name = request.GET.get('name')

    result = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(result.text)

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    picked = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(picked))

    if matched == 6:
        result = '1등입니다. 퇴사!'
    elif matched == 5:
        result = '3등입니다. 휴가!'
    elif matched == 4:
        result = '4등입니다. 자라!'
    elif matched == 3:
        result = '5등입니다. 로또!'
    else:
        result = '기부 ㄱㅅ'

    context = {'name': name, 'result': result}

    return render(request, 'pages/pick_lotto.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    #1. form 태그로 날린 데이터를 받는다.
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 font 리스트 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. font(list) 안에 들어있는 요소 중 하나를 선택해서 font에 저장한다.
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 랜덤하게 뽑은 font를 가지고 다시 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'result': result}

    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd}

    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')