from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    # request: 주소창에 있는 name과 message를 가져오기 위한 기능
    # name: 김영동 / message: 다녀감
    user = request.args.get('user') # 김영동
    message = request.args.get('message')  # 다녀감
    return render_template('receive.html', user=user, message=message)


@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto = response.json()

    #참고: response.text -> string 반환

    ## list comprehension
    # a = [n*2 for n in range(1, 7)] # -> [2, 4, 6, 8, 10, 12]
    a = [lotto[(f'drwtNo{n}')] for n in range(1, 7)]
    b = lotto[(f'bnusNo')]

    winner = f'{a} + {b}'

    ## lotto_check에 있는 my_numbers 가져오기
    my_numbers = [int(n) for n in request.args.get("my_numbers").split()]

    ## 같은 숫자 찾기
    # set()은 수학의 집합과 비슷하다. 리스트와 다르게 순서는 상관이 없다.
    # set(a) & set(my_numbers)    # a와 my_numbers의 교집합 찾기
    matched = len(set(a) & set(my_numbers)) # a와 my_numbers의 교집합 갯수 찾기

    ## 같은 숫자의 갯수에 따른 등수
    if matched == 6:
        result = "축하합니다. 1등입니다."
    elif matched == 5:
        if lotto['bnusNo'] in my_numbers:
            result = "축하합니다. 2등입니다."
        else:
            result = "축하합니다. 3등입니다."
    elif matched == 4:
        result = "축하합니다. 4등입니다."
    elif matched == 3:
        result = "축하합니다. 5등입니다."
    else:
        result = "꽝입니다. 다음 기회에..."


    return render_template('lotto_result.html', lotto = winner, lotto_round = lotto_round, my_numbers = my_numbers, result = result)

if __name__ == '__main__':
    app.run(debug=True)