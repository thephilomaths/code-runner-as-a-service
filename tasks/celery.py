from celery import Celery

app = Celery('tasks.tasks')

app.config_from_object('tasks.celeryconfig')
