from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def front():
    return render_template('front_page.html')

@app.route('/input')
def input():
    return render_template('input_page.html')

@app.route('/output')
def output():
    user = request.args.get('user')
    colors = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
    for i in random.choices(colors):
        return render_template('output_page.html', user=user, contents = i)


if __name__ == '__main__':
    app.run(debug=True)