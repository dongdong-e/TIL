from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
# request는 필수요소!
# html 이름은 함수와 동일하게 만듦
def index(request):
    return render(request, 'index.html')

def hola(request):
    return render(request, 'hola.html')

# 통상적으로 context를 사용한다.
def dinner(request):
    menu = ['짜장면', '샐러드', '햄버거', '스파게티', '치킨']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name': name,
               'age': age}
    return render(request, 'introduce.html', context)

def times(request, num1, num2):
    context = {'num1': num1,
               'num2': num2,
               'result': num1 * num2}
    return render(request, 'times.html', context)

def area(request, num1):
    num2 = 3.14
    context = {'num1': num1,
               'result': num1**2 * num2}
    return render(request, 'area.html', context)

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
    return render(request, 'template_language.html', context)

def birth_day(request):
    today = datetime.today().strftime('%m-%d')

    birth_date = '09-02'

    if today == birth_date:
        context = {'result': '생일 축하합니다.'}
    else:
        context = {'result': '오늘은 생일이 아니군요.'}

    return render(request, 'birth_day.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message_01 = request.GET.get('message_01')
    message_02 = request.GET.get('message_02')
    context = {'message_01': message_01,
               'message_02': message_02}
    return render(request, 'catch.html', context)

def lotto(request):
    return render(request, 'lotto.html')

def lotto_number(request):
    if '로또' in request.GET.get('message'):
        lotto_number = sorted(random.sample(range(1, 46), 6))
        context = {'lotto_number': lotto_number}
    return render(request, 'lotto_number.html', context)