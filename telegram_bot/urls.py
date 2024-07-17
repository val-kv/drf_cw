from django.urls import path
from .views import send_reminder

app_name = 'telegram_bot'

urlpatterns = [
    path('send_reminder/', send_reminder, name='send_reminder'),
]