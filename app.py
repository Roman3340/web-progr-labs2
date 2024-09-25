from flask import Flask, redirect, url_for
app = Flask(__name__)

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
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h2>web-сервер на flask</h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
        </ul>

        <footer>
            &copy; Чукаев Роман, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Чукаев Роман Константинович, лабораторная 1</title>
    </head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <div>
            <a href="http://127.0.0.1:5000/menu">
                <img src="''' + url_for('static', filename='strelka.png') + '''" class='strelka'>
            </a>
            <a href="http://127.0.0.1:5000/menu" class='backmenu'>Вернуться в меню</a>
        </div>
        <h2>
            Реализованные роуты
        </h2>

        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">Дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/telegram">Telegram</a></li>
        </ul>
        <footer>
            &copy; Чукаев Роман, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1 style='padding-left: 15px'>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" class='oak'>
        <div>
            <a href="http://127.0.0.1:5000/lab1">
                <img src="''' + url_for('static', filename='strelka.png') + '''" class='strelka'>
            </a>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Чукаев Роман Константинович</h1>
        <img src="''' + url_for('static', filename='nstu.png') + '''" class='nstu'>
        <div>
            <a href="http://127.0.0.1:5000/lab1">
                <img src="''' + url_for('static', filename='strelka.png') + '''" class='strelka'>
            </a>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Python</h1>
        <p>
            Python – это высокоуровневый язык программирования, который был разработан в конце 1980-х годов. Его разработчик, Гвидо ван Россум, вложил в основу языка простоту и читабельность кода, что позволяет использовать Python для быстрой и эффективной разработки. Много популярных веб-сайтов, компьютерных игр и программ, написанных на Python, вы используете ежедневно: Dropbox, Uber, Sims, Google, GIMP и другие.
        </p>
        <p>
            У Python большая библиотека сторонних модулей и инструментов, что делает его мощным инструментом. Наличие активного сообщества разработчиков позволяет постоянно поддерживать и обновлять язык, предоставлять достаточный объем обучающих материалов, документацию и форумы для программистов с любым уровнем знаний.
        </p>
        <img src="''' + url_for('static', filename='python.png') + '''" class='python'>
        <div>
            <a href="http://127.0.0.1:5000/lab1">
                <img src="''' + url_for('static', filename='strelka.png') + '''" class='strelka'>
            </a>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''

@app.route('/lab1/telegram')
def telegram():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Telegram</h1>
        <p>
           Telegram — самое популярное приложение для обмена мгновенными сообщениями в некоторых странах Европы, Азии и Африки. По словам Павла Дурова, на начало 2023 года Telegram стал вторым после WhatsApp мессенджером в мире по популярности[10]. По состоянию на июль 2024 года Telegram насчитывает более 950 миллионов ежемесячных активных пользователей[11], по количеству пользователей лидирует Индия[12]. Серверы Telegram расположены по всему миру в нескольких дата-центрах, а штаб-квартира находится в Дубае, Объединённые Арабские Эмираты.
        </p>
        <p>
           Павел Дуров, активно выступающий за свободу интернета, утверждает, что Telegram имеет высокую степень конфиденциальности данных. По оценкам СМИ, такая политика конфиденциальности привлекла в Telegram террористов, экстремистов, мошенников, торговцев оружием и наркотиками. По данным Surfshark, всего Telegram временно или бессрочно блокировали в 31 стране[13]. Расследование, связанное с организованной преступностью в Telegram стало причиной уголовного преследования Павла Дурова во Франции в 2024 году.
        </p>
        <img src="''' + url_for('static', filename='telegram.png') + '''" class='telegram'>
        <div>
            <a href="http://127.0.0.1:5000/lab1">
                <img src="''' + url_for('static', filename='strelka.png') + '''" class='strelka'>
            </a>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''

@app.route('/lab2/a/')
def a():
    return 'ok'

@app.route('/lab2/a')
def ae():
    return 'okey'


flower_list = ('роза', 'тюльпан', 'незабудка', 'ромашка')

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return 'цветок: ' + flower_list[flower_id]