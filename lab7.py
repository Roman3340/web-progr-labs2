from flask import Blueprint, render_template, request, abort, jsonify, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path
lab7 = Blueprint('lab7', __name__)


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'roman_chukaev_knowledge_base',
        user = 'roman_chukaev_knowledge_base',
        password = '123'
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

# films = [
#     {
#         'title': 'Forrest Gump',
#         'title_ru': 'Форрест Гамп',
#         'year': 1994,
#         'description': 'Сидя на автобусной остановке, Форрест Гамп — не очень умный, но добрый и открытый парень — рассказывает случайным \
#         встречным историю своей необыкновенной жизни. С самого малолетства парень страдал от заболевания ног, соседские мальчишки дразнили \
#         его, но в один прекрасный день Форрест открыл в себе невероятные способности к бегу. Подруга детства Дженни всегда его поддерживала \
#         и защищала, но вскоре дороги их разошлись.'
#     },
#     {
#         'title': 'The Gentlemen',
#         'title_ru': 'Джентльмены',
#         'year': 2019,
#         'description': 'Один ушлый американец ещё со студенческих лет приторговывал наркотиками, а теперь придумал схему нелегального обогащения \
#             с использованием поместий обедневшей английской аристократии и очень неплохо на этом разбогател. Другой пронырливый журналист приходит \
#             к Рэю, правой руке американца, и предлагает тому купить киносценарий, в котором подробно описаны преступления его босса при участии \
#             других представителей лондонского криминального мира — партнёра-еврея, китайской диаспоры, чернокожих спортсменов и даже русского олигарха.'
#     },
#     {
#         'title': "Hachi: A Dog's Tale",
#         'title_ru': 'Хатико: Самый верный друг',
#         'year': 2008,
#         'description': 'Однажды, возвращаясь с работы, профессор колледжа нашел на вокзале симпатичного щенка породы акита-ину. Профессор и Хатико стали верными друзьями. Каждый день пес провожал и встречал хозяина на вокзале.'
#     },
#     {
#         'title': "Harry Potter and the Sorcerer's Stone",
#         'title_ru': 'Гарри Поттер и философский камень',
#         'year': 2001,
#         'description': 'Жизнь десятилетнего Гарри Поттера нельзя назвать сладкой: родители умерли, едва ему исполнился год, а от дяди и тёти, взявших \
#         сироту на воспитание, достаются лишь тычки да подзатыльники. Но в одиннадцатый день рождения Гарри всё меняется. Странный гость, неожиданно \
#         появившийся на пороге, приносит письмо, из которого мальчик узнаёт, что на самом деле он - волшебник и зачислен в школу магии под названием Хогвартс. \
#         А уже через пару недель Гарри будет мчаться в поезде Хогвартс-экспресс навстречу новой жизни, где его ждут невероятные приключения, верные друзья и \
#         самое главное — ключ к разгадке тайны смерти его родителей.'
#     },
#     {
#         'title': 'The Matrix',
#         'title_ru': 'Матрица',
#         'year': 1999,
#         'description': 'Жизнь Томаса Андерсона разделена на две части: днём он — самый обычный офисный работник, получающий нагоняи от начальства, а ночью \
#         превращается в хакера по имени Нео, и нет места в сети, куда он бы не смог проникнуть. Но однажды всё меняется. Томас узнаёт ужасающую правду о реальности.'
#     }
# ]

# @lab7.route('/lab7/rest-api/films/', methods=['GET'])
# def get_films():
#     return jsonify(films)

# @lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
# def get_film(id):
#     if 0 <= id < len(films):
#         return films[id]
#     else:
#         abort(404)


# @lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
# def delete_film(id):
#     if 0 <= id < len(films):
#         del films[id]
#         return '', 204
#     else:
#         abort(404)

# @lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
# def put_film(id):
#     if id < 0 or id >= len(films):
#         abort(404)
#     film = request.get_json()
#     if film ['description'] == '':
#         return {'description': 'Заполните описание'}, 400
#     elif len(film['description']) > 2000:
#         return {'description': 'Описание не должно превышать 2000 символов'}, 400
#     if not film.get('title') and not film.get('title_ru'):
#         return {'title': 'Заполните поля с названиями/только русское'}, 400
#     if not film.get('title_ru'):
#         return {'title_ru': 'Заполните русское название'}, 400
#     if not film.get('title'):
#         film['title'] = film['title_ru']
#     if not film.get('year'):
#         return {'year': 'Заполните год выпуска фильма'}, 400
#     if int(film ['year']) < 1895 or int(film ['year']) > 2024:
#         return {'year': 'Введите правильный год (от 1895 до 2024)'}, 400
#     films[id] = film
#     return films[id]

# @lab7.route('/lab7/rest-api/films/', methods=['POST'])
# def add_film():
#     film = request.get_json()
#     if not film:
#         abort(404)
#     if film.get('description', '') == '':
#         return {'description': 'Заполните описание'}, 400
#     elif len(film['description']) > 2000:
#         return {'description': 'Описание не должно превышать 2000 символов'}, 400
#     if not film.get('title') and not film.get('title_ru'):
#         return {'title': 'Заполните поля с названиями/только русское'}, 400
#     if not film.get('title_ru'):
#         return {'title_ru': 'Заполните русское название'}, 400
#     if not film.get('title'):
#         film['title'] = film['title_ru']
#     if not film.get('year'):
#         return {'year': 'Заполните год выпуска фильма'}, 400
#     elif int(film['year']) < 1895 or int(film['year']) > 2024:
#         return {'year': 'Введите правильный год (от 1895 до 2024)'}, 400
#     films.append(film)
#     return {'id': len(films) - 1}, 201



# Подключение к базе данных
def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='roman_chukaev_knowledge_base',
            user='roman_chukaev_knowledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

# Валидация данных
def validate_film_data(film):
    errors = {}
    if not film.get('title') and not film.get('title_ru'):
        errors['title'] = 'Заполните поля с названиями/только русское'
    if not film.get('title_ru'):
        errors['title_ru'] = 'Заполните русское название'
    if not film.get('year'):
        errors['year'] = 'Заполните год выпуска фильма'
    elif not (1895 <= int(film['year']) <= 2024):
        errors['year'] = 'Введите правильный год (от 1895 до 2024)'
    if film.get('description', '') == '':
        errors['description'] = 'Заполните описание'
    elif len(film['description']) > 2000:
        errors['description'] = 'Описание не должно превышать 2000 символов'
    return errors

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films_route():
    conn, cur = db_connect()
    try:
        cur.execute("SELECT * FROM films")
        films = cur.fetchall()
        return jsonify(films)
    finally:
        db_close(conn, cur)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film_route(id):
    conn, cur = db_connect()
    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM films WHERE id = %s", (id,))
        else:
            cur.execute("SELECT * FROM films WHERE id = ?", (id,))
        film = cur.fetchone()
        if film:
            return jsonify(film)
        else:
            abort(404)
    finally:
        db_close(conn, cur)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film_route(id):
    film = request.get_json()
    if not film:
        abort(400, 'No input data provided')

    errors = validate_film_data(film)
    if errors:
        return jsonify(errors), 400

    conn, cur = db_connect()
    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                "UPDATE films SET title = %s, title_ru = %s, year = %s, description = %s WHERE id = %s",
                (film['title'], film['title_ru'], film['year'], film['description'], id)
            )
        else:
            cur.execute(
                "UPDATE films SET title = ?, title_ru = ?, year = ?, description = ? WHERE id = ?",
                (film['title'], film['title_ru'], film['year'], film['description'], id)
            )
        if cur.rowcount > 0:
            return jsonify(film)
        else:
            abort(404)
    finally:
        db_close(conn, cur)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def delete_film_route(id):
    conn, cur = db_connect()
    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("DELETE FROM films WHERE id = %s", (id,))
        else:
            cur.execute("DELETE FROM films WHERE id = ?", (id,))
        if cur.rowcount > 0:
            return '', 204
        else:
            abort(404)
    finally:
        db_close(conn, cur)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def post_film_route():
    film = request.get_json()
    if not film:
        abort(400)

    errors = validate_film_data(film)
    if errors:
        return jsonify(errors), 400

    conn, cur = db_connect()
    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                "INSERT INTO films (title, title_ru, year, description) VALUES (%s, %s, %s, %s) RETURNING id",
                (film['title'], film['title_ru'], film['year'], film['description'])
            )
            new_film_id = cur.fetchone()['id']
        else:
            cur.execute(
                "INSERT INTO films (title, title_ru, year, description) VALUES (?, ?, ?, ?)",
                (film['title'], film['title_ru'], film['year'], film['description'])
            )
            new_film_id = cur.lastrowid
        return jsonify({'id': new_film_id}), 201
    finally:
        db_close(conn, cur)
