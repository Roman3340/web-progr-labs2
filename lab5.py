from flask import Blueprint, render_template, request, current_app
import psycopg2
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    try:
        # Попытка соединения с базой данных
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='roman_chukaev_knowledge_base',
            user='roman_chukaev_knowledge_base',
            password='123'
        )
        cur = conn.cursor()

        # Проверка на существование пользователя
        cur.execute("SELECT login_user FROM users WHERE login_user = %s;", (login,))
        if cur.fetchone():
            cur.close()
            conn.close()
            return render_template('lab5/register.html', error='Такой пользователь уже существует')

        # Вставка нового пользователя
        cur.execute("INSERT INTO users (login_user, password_user) VALUES (%s, %s);", (login, password))
        conn.commit()
        cur.close()
        conn.close()
        return render_template('lab5/success.html', login=login, error=None)

    except psycopg2.Error as db_error:
        # Логирование ошибки базы данных
        current_app.logger.error(f"Ошибка базы данных: {db_error}")
        return render_template('lab5/register.html', error="Ошибка подключения к базе данных")
    