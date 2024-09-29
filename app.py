from flask import Flask, redirect, url_for, render_template
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
            <li><a href="http://127.0.0.1:5000/lab2">Вторая лабораторная</a></li>
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

all_flower_list = [
    {'name': 'роза', 'kolvo': 5},
    {'name': 'тюльпан', 'kolvo': 15},
    {'name': 'гипсофила', 'kolvo': 10},
    {'name': 'ромашка', 'kolvo': 20},
]
  

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(all_flower_list):
        return "Такого цветка нет", 404
    else:
        return render_template('flowers_ids.html', flower_id=flower_id, flower=all_flower_list[flower_id])



@app.route('/lab2/flower/<name>')
def add_flower(name):
    # Проверим, есть ли уже цветок с таким именем, если нет - добавим новый
    for flower in all_flower_list:
        if flower['name'] == name:
            return f"Цветок с именем {name} уже существует.", 400
    
    all_flower_list.append({'name': name, 'kolvo': 1})  # добавляем цветок с количеством 1 по умолчанию
    return redirect(url_for('all_flowers'))

@app.route('/lab2/flower/')
def no_flower():
    return "Вы не задали имя цветка", 400   

@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template('flowers.html', all_flower_list=all_flower_list)


@app.route('/lab2/flowers/clear')
def clear_flowers():
    all_flower_list.clear()
    return redirect(url_for('all_flowers'))

@app.route('/lab2/example')
def example():
    name = 'Роман Чукаев'
    numberOfLab = '2'
    groupStudent = 'ФБИ-24'
    numberOfCourse = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name=name, numberOfLab=numberOfLab,
                           groupStudent=groupStudent, numberOfCourse=numberOfCourse, 
                           fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий чудных...'
    return render_template('filter.html', phrase=phrase)


@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)


@app.route('/lab2/calc/')
def calc_without_numbers():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>/')
def calc_with_a(a):
    return redirect(url_for('calc', a=a, b=1))


book_list = [
    {'author': 'Джеймс Дж.', 'name': 'Улисс', 'ganre': 'роман', 'numbOfPages': 1056},
    {'author': 'Драйзер Т.', 'name': 'Трилогия желаний', 'ganre': 'роман', 'numbOfPages': 1152},
    {'author': 'Лев Толстой', 'name': 'Война и мир', 'ganre': 'роман-эпопея', 'numbOfPages': 1360},
    {'author': 'Голсуорси Дж.', 'name': 'Сага о форсайтах', 'ganre': 'роман', 'numbOfPages': 1376},
    {'author': 'Солженицын А.', 'name': 'Архипелаг ГУЛАГ', 'ganre': 'опыт художественного исследования', 'numbOfPages': 1424},
    {'author': 'Палиссер Ч.', 'name': 'Квинканкс', 'ganre': 'роман', 'numbOfPages': 1472},
    {'author': 'Манн Т.', 'name': 'Иосиф и его братья', 'ganre': 'роман', 'numbOfPages': 1492},
    {'author': 'Пруст М.', 'name': 'В поисках утраченного времени', 'ganre': 'роман', 'numbOfPages': 3031},
    {'author': 'Кнаусгор К.', 'name': 'Моя борьба ', 'ganre': 'автобиография', 'numbOfPages': 3600}
]

@app.route('/lab2/books')
def books():
    return render_template('books.html', book_list=book_list)


@app.route('/lab2/mops')
def mops():
    mops_list = [
    {'title': 'Мопс-лягушонок', 'photo': url_for('static', filename='mops1.jpg'), 'description': 'Это мопс, или это лягушонок? Совсем не понимаю, вроде хрюкает, лягушки же не хрюкают... Но вроде и зелененький, как лягушонок...'},
    {'title': 'Голодный мопс', 'photo': url_for('static', filename='mops2.jpg'), 'description': 'Этого мопса покормили 3 минуты назад, и он снова хочет есть, что за дела? А ну слезь со стола, эта печенька не для тебя!'},
    {'title': 'Мопс-невдупленыш', 'photo': url_for('static', filename='mops3.jpg'), 'description': 'Он ещё совсем маленький, и совсем не понимает кто он и что он, ему лишь бы поесть и поспать. Боже, как я его понимаю...'},
    {'title': 'Странные мопсы', 'photo': url_for('static', filename='mops4.jpg'), 'description': 'А вы заметили вообще, что это и не мопсы совсем, это же варежки! Вот это технологии пошли конечно, такое мог придумать только русский человек, у других бы смекалочки не хватило!'},
    {'title': 'Чилльный мопс', 'photo': url_for('static', filename='mops5.jpg'), 'description': 'Ну тут и так все понятно, мопс на выходных, добавить нечего.'},
    {'title': 'Соблазнительный мопс', 'photo': url_for('static', filename='mops6.jpg'), 'description': 'Вы только посмотрите на эти горячие булочки, признайтесь, захотелось??? Мне вот да.'}
]
    return render_template('mops.html', mops_list=mops_list)