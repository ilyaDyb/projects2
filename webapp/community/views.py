from flask import Blueprint, render_template
from webapp.community.discussions.models import Discussions
from webapp.user.models import User

blueprint = Blueprint("community", __name__)


@blueprint.route('/community')
def community_page():
    discussions_json = []
    discussions_list = Discussions.query.filter(Discussions.title.isnot(None)).order_by(Discussions.date.desc()).all()
    for discussion in discussions_list:
        discussions_json.append(
            {
                "id": discussion.id,
                "title": discussion.title,
                "text": discussion.text,
                "date": discussion.date,
                "username": User.query.filter_by(id=discussion.autor).first().username,
                "answer_count": discussion.answer_count()
            }
        )

    return render_template("community.html", discussions_json=discussions_json)
