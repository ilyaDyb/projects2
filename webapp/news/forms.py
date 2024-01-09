from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from webapp.news.models import News


class CommentForm(FlaskForm):
    news_id = HiddenField('ID', validators=[DataRequired()])
    comment_text = StringField("Your comment", validators=[DataRequired()], render_kw={"class": 'form-control'})
    submit = SubmitField('Send', render_kw={"class": "submit"})

    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError("News id error")


class GetSubscribe(FlaskForm):
    submit = SubmitField('Subscribe', render_kw={"class": "btn__submit"})