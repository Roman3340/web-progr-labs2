from flask import Blueprint, render_template, request, redirect, abort, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, articles

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    login_exist = users.query.filter_by(login = login_form).first()
    if login_exist:
        return render_template('lab8/register.html', error = 'Такой пользователь уже существует')
    
    if not (login_form or password_form):
        return render_template('lab8/register.html', error = 'Заполните все поля')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/lab8/')