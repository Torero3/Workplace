# app/home/routes.py

from app.home       import home
from flask          import render_template

from flask          import session, redirect, url_for, request, flash, abort
from flask_login    import login_required, current_user

@home.route('/')
@home.route('/home')
def home():
    print("Home function called!")
    user = {'username': 'Raúl'}
    return render_template('home.html', title='Home', user=user)