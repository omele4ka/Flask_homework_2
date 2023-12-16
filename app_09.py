# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key =b'fc77a01da7b8e6109bed65e07a8882cc79ace608cba79ef060704cad30e9d438'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    if request.method == 'POST':
        username = request.form['name']
        useremail = request.form['email']

        response = make_response(redirect(url_for('greet')))
        response.set_cookie('username', username)
        response.set_cookie('useremail', useremail)
        return response
    
@app.route('/greet')
def greet():
    username = request.cookies.get('username')
    return render_template('greet.html', username=username)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    response.delete_cookie('useremail')
    return response


if __name__ == '__main__':
    app.run(debug=True)