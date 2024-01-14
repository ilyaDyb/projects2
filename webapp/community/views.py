from flask import Blueprint, render_template
from webapp.community.discussions.models import Discussions
from webapp.user.models import User

blueprint = Blueprint("community", __name__)


@blueprint.route('/community')
def community_page():
    discussions_json = []
    discussions_list = Discussions.query.filter(Discussions.title.isnot(None)).order_by(Discussions.date.desc()).all()
    for i in discussions_list:
        discussion_id = i.id
        title = i.title
        text = i.text
        date = i.date
        autor_id = i.autor
        autor_username = User.query.filter_by(id=autor_id).first().username
        discussions_json.append(
            {
                "id": discussion_id,
                "title": title,
                "text": text,
                "date": date,
                "username": autor_username,
            }
        )

    return render_template("community.html", discussions_json=discussions_json)
