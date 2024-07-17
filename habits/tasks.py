from celery import shared_task
from telegram import Bot


@shared_task
def send_telegram_notification(chat_id, message):
    bot = Bot(token='7403382176:AAGe4SGM1aCnGDsyG_QXR7K210o3mWwDUzs')
    bot.send_message(chat_id=chat_id, text=message)
