from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня", default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-success"})