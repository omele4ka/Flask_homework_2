# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)


app.secret_key = b'eb2ebbee6952bbbf87f20f2c7a12264a0d6aaa75d85a5d57516b56ee26998ba3' 

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    username = request.form.get('username')
    if request.method == 'POST':
        flash(f'Привет, {username}', 'success')
        return redirect(url_for('hello'))
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)