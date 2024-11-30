from flask import Flask, redirect, url_for, render_template
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)


app.secret_key = 'секретно-секретный секрет'

@app.route("/")
@app.route("/index")
def start():
    return redirect('/menu', code=302)


@app.route('/menu')
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных.
        </header>

        <h2>web-сервер на flask</h2>
        <ul>
            <li><a href="/lab1">Первая лабораторная</a></li>
            <li><a href="/lab2/">Вторая лабораторная</a></li>
            <li><a href="/lab3/">Третья лабораторная</a></li>
            <li><a href="/lab4/">Четвертая лабораторная</a></li>
            <li><a href="/lab5/">Пятая лабораторная</a></li>
            <li><a href="/lab6/">Шестая лабораторная</a></li>
            <li><a href="/lab7/">Седьмая лабораторная</a></li>
        </ul>

        <footer>
            &copy; Чукаев Роман, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.route('/lab1/')
def lab_1():
    return render_template('lab1')

@app.route('/lab2/')
def lab_2():
    return render_template('lab2/lab2.html')

@app.route('/lab3/')
def lab_3():
    return render_template('lab3/lab3.html')

@app.route('/lab4/')
def lab_4():
    return render_template('lab4/lab4.html')

@app.route('/lab5/')
def lab_5():
    return render_template('lab5/lab5.html')

@app.route('/lab6/')
def lab_6():
    return render_template('lab6/lab6.html')


@app.errorhandler(404)
def not_found_404(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h2>Ошибка 404 - такой страницы не существует</h2>

        <footer>
            &copy; Чукаев Роман, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.errorhandler(500)
def not_found_500(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
        <p>Подробности ошибки: ''' + str(err) + '''</p> 

        <footer>
            &copy; Чукаев Роман, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
''', 500