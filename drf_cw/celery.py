import eventlet
import os
from celery import Celery

eventlet.monkey_patch()

# Создаем экземпляр Celery
app = Celery('drf_cw')

# Загружаем настройки из переменных среды
app.conf.update(
    broker_url=os.environ.get('CELERY_BROKER_URL'),
    result_backend=os.environ.get('CELERY_RESULT_BACKEND'),
    task_serializer=os.environ.get('CELERY_TASK_SERIALIZER'),
    accept_content=os.environ.get('CELERY_ACCEPT_CONTENT'),
    result_serializer=os.environ.get('CELERY_RESULT_SERIALIZER'),
    timezone=os.environ.get('CELERY_TIMEZONE'),
    celery_beat_schedule=os.environ.get('CELERY_BEAT_SCHEDULE'),
)

# Загружаем задачи из модулей
app.autodiscover_tasks()
