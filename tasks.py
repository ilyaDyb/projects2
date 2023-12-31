from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.pasers.habr import get_info_from_habr, get_content_from_habr

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')
"""celery -A tasks worker --loglevel=info
    celery -A tasks beat"""


@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        get_info_from_habr()


@celery_app.task
def habr_content():
    with flask_app.app_context():
        get_content_from_habr()


@celery_app.on_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.app_periodic_task(crontab(minute='*/1'), habr_snippets.s())
    sender.app_periodic_task(crontab(minute='*/1'), habr_content.s())
