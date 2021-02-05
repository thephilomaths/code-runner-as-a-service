import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./') / '.env.development.local'
load_dotenv(dotenv_path=dotenv_path)
env = os.environ

broker_host = env['CELERY_BROKER_HOST']
broker_port = env['CELERY_BROKER_PORT']
broker_user = env['CELERY_BROKER_USER']
broker_password = env['CELERY_BROKER_PASSWORD']

result_backend_user = env['DATABASE_USERNAME']
result_backend_password = env['DATABASE_PASSWORD']
result_backend_host = env['DATABASE_HOST']
result_backend_db = env['DATABASE_NAME']

imports = ("tasks.tasks", )
broker_url = f'pyamqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}'
result_backend = f'db+postgresql://{result_backend_user}:{result_backend_password}@{result_backend_host}/' \
                 f'{result_backend_db}'
result_persistent = True

print(broker_url)