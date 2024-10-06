from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)

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


@app.route('/lab2/a/')
def a():
    return 'ok'

@app.route('/lab2/a')
def ae():
    return 'okey'

all_flower_list = [
    {'name': 'роза', 'kolvo': 5, 'price': 120},
    {'name': 'тюльпан', 'kolvo': 15, 'price': 70},
    {'name': 'гипсофила', 'kolvo': 10, 'price': 100},
    {'name': 'ромашка', 'kolvo': 20, 'price': 80},
]
  

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(all_flower_list):
        return "Такого цветка нет", 404
    else:
        return render_template('flowers_ids.html', flower_id=flower_id, flower=all_flower_list[flower_id])



@app.route('/lab2/flower/<name>')
def add_flower(name):
    for flower in all_flower_list:
        if flower['name'] == name:
            flower['kolvo'] += 1 
            return redirect(url_for('all_flowers'))
    
    all_flower_list.append({'name': name, 'kolvo': 1, 'price': 100})  
    return redirect(url_for('all_flowers'))

@app.route('/lab2/del_flower/<name>')
def del_flower(name):
    for flower in all_flower_list:
        if flower['name'] == name:
            all_flower_list.remove(flower)  # удаляем цветок
            return redirect(url_for('all_flowers'))
    
    return f"Цветок с именем {name} не найден.", 404  

@app.route('/lab2/del_flower/')
def no_del_flower():
    return "Вы не задали имя цветка", 400   

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