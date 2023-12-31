from webapp import create_app
from webapp.news.pasers.habr import get_info_from_habr, get_content_from_habr

app = create_app()
with app.app_context():
    get_info_from_habr()
    # get_content_from_habr()
