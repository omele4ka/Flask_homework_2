# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request


app = Flask(__name__)

@app.get('/')
def index():
    return render_template('number.html')

@app.post('/')
def square_number():
    num = float(request.form.get('num'))
    result = num ** 2
    text = f'Квадрат числа {num} равен '
    return render_template('result.html', text=text, result=result)


if __name__ == '__main__':
    app.run(debug=True)