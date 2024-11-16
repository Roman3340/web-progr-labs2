from flask import Blueprint, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab6 = Blueprint('lab6', __name__)


# offices = []
# for i in range(1, 11):
#     offices.append({'number': i, 'tenant': '', 'price': 900 + i%3})


@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

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


# @lab6.route('/lab6/json-rpc-api/', methods = ['POST'])
# def api():
#     data = request.json
#     id = data['id']
#     if data['method'] == 'info':
#         return {
#             'jsonrpc': '2.0',
#             'result': offices,
#             'id': id
#         }
    
#     login = session.get('login')
#     if not login:
#         return {
#             'jsonrpc': '2.0',
#             'error': {
#                 'code': 1,
#                 'message': 'Unauthorized'
#             },
#             'id': id
#         }
    
#     if data['method'] == 'booking':
#         office_number = data['params']
#         for office in offices:
#             if office['number'] == office_number:
#                 if office['tenant'] != '':
#                     return {
#                     'jsonrpc': '2.0',
#                     'error': {
#                         'code': 2,
#                         'message': 'Alredy booked'
#                     },
#                     'id': id
#                 }
                
#                 office['tenant'] = login
#                 return {
#                     'jsonrpc': '2.0',
#                     'result': 'success',
#                     'id': id
#                 }
        
#     if data['method'] == 'cancellation':
#         office_number = data['params']
#         for office in offices:
#             if office['number'] == office_number:
#                 if not office['tenant']:
#                     return {
#                         'jsonrpc': '2.0',
#                         'error': {
#                             'code': 3,
#                             'message': 'Not rented'
#                         },
#                         'id': id
#                     }
#                 if office['tenant'] != login:
#                     return {
#                         'jsonrpc': '2.0',
#                         'error': {
#                             'code': 4,
#                             'message': 'Doesnt belong to you',
#                             'id': id
#                         }
#                     }
#                 office['tenant'] = ''
#                 return {
#                     'jsonrpc': '2.0',
#                     'result': 'success',
#                     'id': id
#                 }
    
#     return {
#         'jsonrpc': '2.0',
#         'error': {
#             'code': -32601,
#             'message': 'Method not found'
#         },
#         'id': id
#     }


@lab6.route('/lab6/json-rpc-api/', methods = ['POST'])
def api():
    data = request.json
    method = data.get('method')
    id = data.get('id')

    # Проверка авторизации
    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {'code': 1, 'message': 'Unauthorized'},
            'id': id
        }

    conn, cur = db_connect()

    if method == 'info':
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT office_number, office_tenant, price FROM offices")
        else:
            cur.execute("SELECT office_number, office_tenant, price FROM offices")
        
        offices = cur.fetchall()
        office_list = [{'number': office['office_number'], 
                        'tenant': office['office_tenant'], 
                        'price': office['price']} for office in offices]

        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': office_list,
            'id': id
        }

    if method == 'booking':
        office_number = data.get('params')

        # Получаем user_id по логину
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT id FROM users WHERE login_user=%s", (login,))
        else:
            cur.execute("SELECT id FROM users WHERE login_user=?", (login,))
        
        user = cur.fetchone()
        if not user:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {'code': 1, 'message': 'User not found'},
                'id': id
            }

        user_id = user['id']  # Получаем user_id



        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT office_tenant FROM offices WHERE office_number=%s", (office_number,))
        else:
            cur.execute("SELECT office_tenant FROM offices WHERE office_number=?", (office_number,))
        
        office = cur.fetchone()
        if not office or office['office_tenant']:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {'code': 2, 'message': 'Already booked'},
                'id': id
            }

        # Бронирование офиса
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("UPDATE offices SET office_tenant=%s, user_id=%s WHERE office_number=%s", (login, user_id, office_number))
        else:
            cur.execute("UPDATE offices SET office_tenant=?, user_id=? WHERE office_number=?", (login, user_id, office_number))

        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    if method == 'cancellation':
        office_number = data.get('params')

        # Проверяем, арендован ли офис текущим пользователем
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT office_tenant FROM offices WHERE office_number=%s", (office_number,))
        else:
            cur.execute("SELECT office_tenant FROM offices WHERE office_number=?", (office_number,))
        
        office = cur.fetchone()
        if not office or not office['office_tenant']:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {'code': 3, 'message': 'Not rented'},
                'id': id
            }
        if office['office_tenant'] != login:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {'code': 4, 'message': 'Does not belong to you'},
                'id': id
            }

        # Освобождаем офис
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("UPDATE offices SET office_tenant=NULL, user_id=NULL WHERE office_number=%s", (office_number,))
        else:
            cur.execute("UPDATE offices SET office_tenant=NULL, user_id=NULL WHERE office_number=?", (office_number,))

        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    db_close(conn, cur)
    return {
        'jsonrpc': '2.0',
        'error': {'code': -32601, 'message': 'Method not found'},
        'id': id
    }