from __future__ import absolute_import, unicode_literals
import os
from my_celery import Celery


# Установка переменной окружения для настройки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_cw.settings')

app = Celery('drf_cw')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


def shared_task():
    return None
