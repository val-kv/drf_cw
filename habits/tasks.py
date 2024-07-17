from celery import shared_task
from telegram_bot.models import Reminder


@shared_task
def send_telegram_reminder(reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    reminder.send_telegram_reminder()
