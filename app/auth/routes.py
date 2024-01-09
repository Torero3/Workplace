# app/auth/routes.py

from app.auth           import auth
from flask              import render_template, flash, redirect, url_for, session
from app.auth.forms     import UserLoginForm, FirmaLoginForm
from flask_login        import login_user, logout_user, current_user, login_required
from werkzeug.security  import generate_password_hash, check_password_hash
from .                  import auth
from .forms             import UserRegistrationForm, FirmaRegistrationForm

from app.models         import User, Firma
from app                import db


#User Registrierung
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now log in.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

#Firma Registrierung
@auth.route('/registerf', methods=['GET', 'POST'])
def registerf():
    form = FirmaRegistrationForm()
    if form.validate_on_submit():
        firma = Firma(
            fusername=form.fusername.data,
            femail=form.femail.data,
            fpassword_hash=generate_password_hash(form.fpassword.data),
        )
        db.session.add(firma)
        db.session.commit()
        flash('Registration successful. You can now log in.')
        return redirect(url_for('auth.loginf'))
    return render_template('registerf.html', title='Register', form=form)


#User Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            session["_table"] = "User"
            flash('Login erfolgreich!')
            return redirect(url_for('home.home'))
        else:
            flash('Ungültige Anmeldedaten. Bitte erneut versuchen.', 'error')
    return render_template('login.html', title='Anmelden', form=form)

#Firma Login
@auth.route('/loginf', methods=['GET', 'POST'])
def loginf():
    form = FirmaLoginForm()
    if form.validate_on_submit():
        firma = Firma.query.filter_by(fusername=form.fusername.data).first()  
        if firma and check_password_hash(firma.fpassword_hash, form.fpassword.data):
            login_user(firma, remember=form.remember_me.data)
            session["_table"] = "Firma"
            flash('Firma-Login erfolgreich!')
            return redirect(url_for('home.home'))
        else:
            flash('Ungültige Anmeldedaten. Bitte erneut versuchen.', 'error')
    return render_template('loginf.html', title='Anmelden', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user() or logout_firma()
    flash('Sie wurden abgemeldet.')
    return redirect(url_for('home.home'))
