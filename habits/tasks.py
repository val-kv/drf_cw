from my_celery import shared_task
from telegram import Bot


@shared_task
def send_telegram_notification(chat_id, message):
    bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
    bot.send_message(chat_id=chat_id, text=message)
