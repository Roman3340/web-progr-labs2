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



@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    error = None
    temperature_message = None
    snowflakes = ""

    if request.method == 'POST':
        temp = request.form.get('temperature')

        if not temp:
            error = "Ошибка: не задана температура"
        else:
            try:
                temp = int(temp)  # Преобразуем значение в целое число
                if temp < -12:
                    error = "Не удалось установить температуру — слишком низкое значение"
                elif temp > -1:
                    error = "Не удалось установить температуру — слишком высокое значение"
                else:
                    # Проверяем, в каком диапазоне находится температура
                    if -12 <= temp <= -9:
                        temperature_message = f"Установлена температура: {temp}°С"
                        snowflakes = "❄️ ❄️ ❄️"  # Три снежинки
                    elif -8 <= temp <= -5:
                        temperature_message = f"Установлена температура: {temp}°С"
                        snowflakes = "❄️ ❄️"  # Две снежинки
                    elif -4 <= temp <= -1:
                        temperature_message = f"Установлена температура: {temp}°С"
                        snowflakes = "❄️"  # Одна снежинка
            except ValueError:
                error = "Ошибка: введите числовое значение температуры"

    return render_template('/lab4/fridge.html', error=error, temperature_message=temperature_message, snowflakes=snowflakes)


@lab4.route('/lab4/grain-order', methods=['GET', 'POST'])
def grain_order():
    grains = {
        'barley': {'name': 'ячмень', 'price': 12345},
        'oats': {'name': 'овёс', 'price': 8522},
        'wheat': {'name': 'пшеница', 'price': 8722},
        'rye': {'name': 'рожь', 'price': 14111}
    }
    
    error = None
    success_message = None
    discount_message = None

    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        # Проверяем наличие веса
        if not weight:
            error = "Ошибка: не указан вес."
        else:
            try:
                weight = float(weight)
                if weight <= 0:
                    error = "Ошибка: вес должен быть больше 0."
                elif weight > 500:
                    error = "Ошибка: такого объёма сейчас нет в наличии."
                else:
                    # Получаем цену за выбранное зерно
                    grain_info = grains.get(grain_type)
                    if not grain_info:
                        error = "Ошибка: неверный тип зерна."
                    else:
                        price_per_ton = grain_info['price']
                        total_price = weight * price_per_ton

                        # Применяем скидку за большой объем
                        if weight > 50:
                            discount = total_price * 0.10
                            total_price -= discount
                            discount_message = f"Применена скидка 10% за объём. Размер скидки: {discount:.2f} руб."

                        # Формируем сообщение об успешном заказе
                        success_message = f"Заказ успешно сформирован. Вы заказали {grain_info['name']}. Вес: {weight:.2f} т. Сумма к оплате: {total_price:.2f} руб."
            except ValueError:
                error = "Ошибка: введите корректное числовое значение веса."

    return render_template('/lab4/grain-order.html', error=error, success_message=success_message, discount_message=discount_message)




@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    errors = {}

    if request.method == 'POST':
        login = request.form.get('login', '').strip()
        password = request.form.get('password', '').strip()
        name = request.form.get('name', '').strip()
        gender = request.form.get('gender', '').strip()

        if not login:
            errors['login'] = 'Не введен логин'
        if not password:
            errors['password'] = 'Не введен пароль'
        if not name:
            errors['name'] = 'Не введено имя'
        if gender not in ['male', 'female']:
            errors['gender'] = 'Выберите пол'

        # Проверяем, что логин уникален
        for user in users:
            if user['login'] == login:
                errors['login'] = 'Логин уже существует'

        # Если есть ошибки, возвращаем страницу с ошибками
        if errors:
            return render_template('register.html', errors=errors)

        # Если ошибок нет, добавляем нового пользователя в список
        users.append({'login': login, 'password': password, 'name': name, 'gender': gender})
        return redirect('/lab4/login')

    return render_template('/lab4/register.html', errors=errors)


@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')  # Перенаправляем на логин, если не авторизован

    return render_template('/lab4/users_list.html', users=users, current_user=session['login'])


@lab4.route('/lab4/delete_user', methods=['POST'])
def delete_user():
    if 'login' not in session:
        return redirect('/lab4/login')

    login_to_delete = request.form.get('login')

    global users
    users = [user for user in users if user['login'] != login_to_delete]

    # Удаляем сессию, если пользователь сам себя удалил
    if session['login'] == login_to_delete:
        session.pop('login', None)
        session.pop('user_name', None)
        return redirect('/lab4/login')

    return redirect('/lab4/users')


@lab4.route('/lab4/edit_user', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')

    if request.method == 'POST':
        login = request.form.get('login')
        new_name = request.form.get('name', '').strip()
        new_password = request.form.get('password', '').strip()

        for user in users:
            if user['login'] == login:
                if new_name:
                    user['name'] = new_name
                if new_password:
                    user['password'] = new_password

        session['user_name'] = new_name  # Обновляем имя в сессии, если его изменили
        return redirect('/users')

    # GET-запрос: выводим форму редактирования
    user_login = session['login']
    user = next(user for user in users if user['login'] == user_login)
    return render_template('/lab4/edit_user.html', user=user)