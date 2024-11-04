from flask import Blueprint, render_template, request, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    login = session.get('login', 'Anonymous')
    return render_template('lab5/lab5.html', login=login)


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

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login_user FROM users WHERE login_user=%s;", (login, ))
    else:
        cur.execute("SELECT login_user FROM users WHERE login_user=?;", (login, ))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password)

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login_user, password_user) VALUES (%s, %s);", (login, password_hash))
    else:
        cur.execute("INSERT INTO users (login_user, password_user) VALUES (?, ?);", (login, password_hash))
    db_close(conn, cur)
    return render_template('lab5/success.html', login=login, error=None)
    
@lab5.route('/lab5/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error='Заполните поля')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login_user=%s;", (login, ))
    else:
        cur.execute("SELECT * FROM users WHERE login_user=?;", (login, ))
    user = cur.fetchone()
    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', 
                               error='Логин и/или пароль неверны')
    
    if not check_password_hash(user['password_user'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', 
                               error='Логин и/или пароль неверны')
    
    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)

@lab5.route('/lab5/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    session.pop('password', None)  # Удаляем имя из сессии при выходе
    return redirect('/lab5/login')

@lab5.route('/lab5/create', methods = ['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    if request.method == 'GET':
        return render_template('lab5/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not (title or article_text):
        return render_template('lab5/create_article.html', error='Заполните все поля')
    

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login_user=%s;", (login, ))
    else:
        cur.execute("SELECT * FROM users WHERE login_user=?;", (login, ))
    login_id = cur.fetchone()["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s, %s);", (login_id, title, article_text))
    else:
        cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (?, ?, ?);", (login_id, title, article_text))
    # cur.fetchone()

    db_close(conn, cur)
    return redirect('/lab5')


@lab5.route('/lab5/list')
def list():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login_user=%s;", (login, ))
    else:
        cur.execute("SELECT id FROM users WHERE login_user=?;", (login, ))
    login_id = cur.fetchone()["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE user_id=%s;", (login_id, ))
    else:
        cur.execute("SELECT * FROM articles WHERE user_id=?;", (login_id, ))
    articles = cur.fetchall()

    db_close(conn, cur)
    return render_template('/lab5/articles.html', articles=articles)


@lab5.route('/lab5/delete_article', methods=['POST'])
def delete_article():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    article_id = request.form.get('article_id')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM articles WHERE id=%s AND user_id=(SELECT id FROM users WHERE login_user=%s);", (article_id, login))
    else:
        cur.execute("DELETE FROM articles WHERE id=? AND user_id=(SELECT id FROM users WHERE login_user=?);", (article_id, login))
    
    conn.commit()
    db_close(conn, cur)
    
    return redirect('/lab5/list')

@lab5.route('/lab5/edit_article/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()
    
    if request.method == 'GET':
        # Получаем данные статьи для отображения в форме редактирования
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM articles WHERE id=%s AND user_id=(SELECT id FROM users WHERE login_user=%s);", (article_id, login))
        else:
            cur.execute("SELECT * FROM articles WHERE id=? AND user_id=(SELECT id FROM users WHERE login_user=?);", (article_id, login))
        
        article = cur.fetchone()
        db_close(conn, cur)

        if not article:
            return redirect('/lab5/list')

        return render_template('lab5/edit_article.html', article=article)

    # Обработка обновленных данных статьи (POST)
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not (title and article_text):
        return render_template('lab5/edit_article.html', error='Заполните все поля', article={'id': article_id, 'title': title, 'article_text': article_text})

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE articles SET title=%s, article_text=%s WHERE id=%s AND user_id=(SELECT id FROM users WHERE login_user=%s);", (title, article_text, article_id, login))
    else:
        cur.execute("UPDATE articles SET title=?, article_text=? WHERE id=? AND user_id=(SELECT id FROM users WHERE login_user=?);", (title, article_text, article_id, login))

    conn.commit()
    db_close(conn, cur)

    return redirect('/lab5/list')
