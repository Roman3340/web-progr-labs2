from flask import Blueprint, redirect, url_for, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)


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
    
    
    # if color:
    #     resp = make_response(redirect('/lab3/settings'))
    #     resp.set_cookie('color', color)
    #     return resp
    
    # color = request.cookies.get('color')
    # resp = make_response(render_template('lab3/settings.html', color=color))
    # return resp





    # resp = make_response(render_template('lab3/settings.html', color=color))
    # if color:
    #     resp.set_cookie('color', color)
    # return resp