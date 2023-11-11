from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from my_blog.models import User


class RegistrationForm(FlaskForm):
    """This is a resigtration form"""
    username = StringField('Username', validators=
                           [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=
                             [DataRequired(), Length(min=8, max=15)])
    confirm_password = PasswordField('Confirm password', validators=
                                     [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
             raise ValidationError('The username is taken')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
             raise ValidationError('email already exist')

class LoginForm(FlaskForm):
    """This is a login form"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=
                             [DataRequired(), Length(min=8, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')