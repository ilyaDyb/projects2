from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.pasers.habr import get_info_from_habr, get_content_from_habr

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379')


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
    sender.add_periodic_task(crontab(minute='*/1'), habr_snippets.s(), name='periodic_habr_snippets')

    sender.add_periodic_task(crontab(minute='*/2'), habr_content.s(), name='periodic_habr_content')

    if not sender.conf.beat_schedule.get('periodic_habr_snippets') or not sender.conf.beat_schedule.get(
            'periodic_habr_content'):
        sender.send_task('periodic_habr_snippets')
        sender.send_task('periodic_habr_content')


celery_app.conf.beat_schedule = {
    'my-scheduled-task': {
        'task': 'path.to.your.task',
        'schedule': 10,  # пример выполнения каждые 10 секунд
    },
}