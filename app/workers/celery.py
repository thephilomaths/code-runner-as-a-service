from celery import Celery

app = Celery('app.workers.tasks')

app.config_from_object('app.workers.celeryconfig')
