from flask import Blueprint, redirect, url_for, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('/lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success_pay():
    price = request.args.get('finalPrice')
    return render_template('/lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bgcolor = request.args.get('bgcolor')
    fontSyze = request.args.get('fontSyze')
    fontStyle = request.args.get('fontStyle')

    # Проверяем, есть ли запрос на изменение параметров
    if color or bgcolor or fontSyze or fontStyle:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bgcolor:
            resp.set_cookie('bgcolor', bgcolor)
        if fontSyze:
            resp.set_cookie('fontSyze', fontSyze)
        if fontStyle:
            resp.set_cookie('fontStyle', fontStyle)
        return resp

    # Если параметры не переданы, просто возвращаем страницу
    return render_template('/lab3/settings.html')
    

@lab3.route('/lab3/formRZHD')
def rzhd_order():
    errors = {}

    # Получаем значения полей из запроса
    fio = request.args.get('fio', None)
    age = request.args.get('age', None)
    bed = request.args.get('bed', None)
    from_city = request.args.get('from', None)
    where_to = request.args.get('whereTo', None)
    date = request.args.get('date', None)
    dop = request.args.getlist('dop')  # Получаем список для доп.услуг

    # Если запрос пришел без параметров (первый раз открываем страницу), просто отобразим форму
    if fio is None and age is None and bed is None and from_city is None and where_to is None and date is None:
        return render_template('/lab3/formRZHD.html', fio='', age='', bed='', from_city='', where_to='', date='', dop=[], errors={})

    # Проверка поля ФИО
    if not fio:
        errors['fio'] = 'Заполните поле ФИО!'

    # Проверка поля Возраст
    if not age:
        errors['age'] = 'Заполните поле Возраст!'
    else:
        age = int(age)
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'

    # Проверка поля Полка
    if not bed:
        errors['bed'] = 'Выберите полку!'

    # Проверка поля Откуда
    if not from_city:
        errors['from'] = 'Укажите город отправления!'

    # Проверка поля Куда
    if not where_to:
        errors['whereTo'] = 'Укажите город назначения!'

    # Проверка поля Дата
    if not date:
        errors['date'] = 'Укажите дату поездки!'

    # Если есть ошибки, отображаем форму с ошибками
    if errors:
        return render_template('/lab3/formRZHD.html', fio=fio, age=age, bed=bed, from_city=from_city, where_to=where_to, date=date, dop=dop, errors=errors)

    # Преобразуем список доп. услуг в строку с разделителем запятой для передачи через URL
    dop_str = ','.join(dop)

    # Для отладки: выводим значения перед редиректом
    print(f"Дополнительные услуги (dop): {dop}")

    # Если ошибок нет, перенаправляем на заполненную форму
    return redirect(url_for('lab3.ticket', fio=fio, age=age, bed=bed, from_city=from_city, where_to=where_to, date=date, dop=dop_str))


@lab3.route('/lab3/ticket')
def ticket():
    fio = request.args.get('fio')
    age = int(request.args.get('age'))
    bed = request.args.get('bed')
    from_city = request.args.get('from_city')
    where_to = request.args.get('where_to')
    date = request.args.get('date')

    # Получаем строку доп. услуг и преобразуем обратно в список
    dop_str = request.args.get('dop', '')
    dop = dop_str.split(',') if dop_str else []

    # Определяем тип билета и начальную стоимость
    if age < 18:
        ticket_type = 'Детский билет'
        price = 700
    else:
        ticket_type = 'Взрослый билет'
        price = 1000

    # Преобразование значений полки
    bed_mapping = {
        'bottomBed': 'Нижняя полка',
        'headerBed': 'Верхняя полка',
        'bottomSideBed': 'Нижняя боковая полка',
        'headerSideBed': 'Верхняя боковая полка'
    }
    bed = bed_mapping.get(bed, 'Не указано')

    # Преобразование названий городов
    city_mapping = {
        'nsk': 'Новосибирск',
        'msk': 'Москва',
        'spb': 'Санкт-Петербург',
        'kzn': 'Казань'
    }
    from_city = city_mapping.get(from_city, 'Не указано')
    where_to = city_mapping.get(where_to, 'Не указано')

    # Добавляем стоимость в зависимости от типа полки
    if bed in ['Нижняя полка', 'Нижняя боковая полка']:
        price += 100

    # Дополнительные услуги
    dop_services = []
    if 'linen' in dop:
        dop_services.append('бельё')
        price += 75
    if 'baggage' in dop:
        dop_services.append('багаж')
        price += 250
    if 'insurance' in dop:
        dop_services.append('страховка')
        price += 150

    if not dop_services:
        dop_services.append('Без дополнительных услуг')

    # Формируем данные для шаблона билета
    ticket_data = {
        'fio': fio,
        'age': age,
        'ticket_type': ticket_type,
        'price': price,
        'bed': bed,
        'from_city': from_city,
        'where_to': where_to,
        'date': date,
        'dop': dop_services
    }

    return render_template('/lab3/ticket.html', ticket=ticket_data)

@lab3.route('/lab3/clearCookie')
def clear_cookie():
    # Список куки, которые нужно удалить
    cookies_to_clear = ['bgcolor', 'color', 'fontStyle']  # Замените на нужные имена куки

    # Создаем response объект
    response = make_response(redirect('/lab3'))  # Перенаправляем пользователя обратно на /lab3/settings
    
    # Перебираем куки, которые хотим удалить
    for cookie in cookies_to_clear:
        if cookie in request.cookies:
            # Очищаем куку, устанавливая ей пустое значение и время истечения в прошлом
            response.set_cookie(cookie, '', expires=0)
    
    return response