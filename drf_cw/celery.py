from my_celery import Celery

app = Celery('drf_cw')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
