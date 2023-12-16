# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, redirect, render_template, url_for, request


app = Flask(__name__)

@app.get('/')
def index():
    return render_template('age.html')

@app.post('/age/')
def check_age():
    username = request.form.get('username')
    age = int(request.form.get('age'))

    if age < 18:
        print('You are too young')
        return redirect(url_for('index'))
    return redirect(url_for('check_passed', name = username))

@app.route('/pass/<name>')
def check_passed(name: str):
    return render_template('welcome.html', context=name)


if __name__ == '__main__':
    app.run(debug=True)