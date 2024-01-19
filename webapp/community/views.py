from flask import Blueprint, render_template, request
from webapp.community.discussions.models import Discussions
from webapp.user.models import User

blueprint = Blueprint("community", __name__)


@blueprint.route('/community')
def community_page():
    discussions_json = []
    per_page = 5
    page = request.args.get('page', 1, type=int)
    discussions_list = Discussions.query.filter(Discussions.title.isnot(None)).order_by(Discussions.date.desc())\
        .paginate(page=page, per_page=per_page)
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

    return render_template("community.html", **locals())
