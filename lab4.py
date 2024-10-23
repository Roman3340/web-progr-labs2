from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены')
    if x2 == '0':
        return render_template('lab4/div.html', error='Делить на ноль нельзя')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0
    if x2 == '':
        x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')


@lab4.route('/lab4/mult', methods = ['POST'])
def mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1
    if x2 == '':
        x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/exp-form')
def exp_form():
    return render_template('lab4/exp-form.html')


@lab4.route('/lab4/exp', methods = ['POST'])
def exp():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '' or x1 == 0 and x2 == 0:
        return render_template('lab4/exp.html', error='Оба поля должны быть заполнены')
    if x1 == 0 or x2 == 0:
        return render_template('lab4/exp.html', error='Поля не должны иметь нулевых значенией')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 ** x2
    return render_template('lab4/exp.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    return redirect ('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей Смирнов', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Боб Марли', 'gender': 'male'},
    {'login': 'max', 'password': '666', 'name': 'Максим Петров', 'gender': 'male'},
    {'login': 'yulia', 'password': '000', 'name': 'Юлия Василевская', 'gender': 'female'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    errors = {}  # Словарь для хранения ошибок

    if request.method == 'GET':
        if 'user_name' in session:  # Проверяем, есть ли имя в сессии
            authorized = True
            user_name = session['user_name']
        else:
            authorized = False
            user_name = ''  # Пустое значение по умолчанию

        return render_template('/lab4/login.html', authorized=authorized, user_name=user_name, errors=errors)

    else:  # Если метод POST, проверяем ввод логина и пароля
        login = request.form.get('login', '').strip()
        password = request.form.get('password', '').strip()

        if not login:  # Проверяем, пуст ли логин
            errors['login'] = 'Не введен логин'
        if not password:  # Проверяем, пуст ли пароль
            errors['password'] = 'Не введен пароль'

        # Если есть ошибки, вернуть форму с ошибками
        if errors:
            return render_template('/lab4/login.html', authorized=False, errors=errors)

        # Проверяем логин и пароль с пользователями
        for user in users:
            if login == user['login'] and password == user['password']:
                # Устанавливаем сессию с именем и логином
                session['login'] = user['login']
                session['user_name'] = user['name']  # Сохраняем имя в сессии
                return redirect('/lab4/login')

        # Если логин и/или пароль неверные
        error = 'Неверные логин и/или пароль'
        return render_template('/lab4/login.html', authorized=False, errors=errors, error=error)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    session.pop('user_name', None)  # Удаляем имя из сессии при выходе
    return redirect('/lab4/login')
