# app/auth/forms.py

from flask_wtf              import FlaskForm
from wtforms                import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators     import DataRequired, Email, EqualTo, ValidationError

import sqlalchemy as sa
from app import db
from app.models import User, Firma


#User Login
class UserLoginForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')

#User Registration
class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already registered.')

#Firma Login
class FirmaLoginForm(FlaskForm):
    fusername = StringField('Firmenname', validators=[DataRequired()])
    fpassword = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Firma Sign In')

#Firma Registration
class FirmaRegistrationForm(FlaskForm):
    fusername = StringField('Firmenname', validators=[DataRequired()])
    femail = StringField('Email', validators=[DataRequired(), Email()])
    fpassword = PasswordField('Password', validators=[DataRequired()])
    fpassword2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('fpassword')])
    submit = SubmitField('Register')

    def validate_fusername(self, field):
        if Firma.query.filter_by(fusername=field.data).first():
            raise ValidationError('Firmenname is already in use.')

    def validate_femail(self, field):
        if Firma.query.filter_by(femail=field.data).first():
            raise ValidationError('Email is already registered.')

