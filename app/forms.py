from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
