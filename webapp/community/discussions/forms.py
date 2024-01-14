from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class DiscussionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()], render_kw={"class": "form-title",
                                                                         "placeholder": "Введите заголовок"})
    text = StringField("Text", validators=[DataRequired()], render_kw={"class": "form-text",
                                                                       "placeholder": "Ваше сообщение"},
                       widget=TextArea())
    submit = SubmitField("Create", render_kw={"class": "btn btn-success"})


class AnswerForm(FlaskForm):
    id = HiddenField("ID", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()], render_kw={"placeholder": "Введите ваш ответ"},
                       widget=TextArea())
    submit = SubmitField("Send")