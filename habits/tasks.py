import telebot
from datetime import datetime

# Создание экземпляра бота
bot = telebot.TeleBot('7403382176:AAGe4SGM1aCnGDsyG_QXR7K210o3mWwDUzs')


# Функция для отправки напоминания
@bot.message_handler(commands=['remind'])
def remind(message):
    text = message.text.split(' ', 1)[1]
    time = datetime.strptime(text.split(' ', 1)[0], '%Y-%m-%d %H:%M')
    reminder = text.split(' ', 1)[1]
    bot.send_message(message.chat.id, reminder, str(datetime.timestamp(time)))


# Запуск бота
bot.polling()
