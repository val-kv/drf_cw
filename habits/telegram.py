import requests


def send_telegram_message(user_chat_id, message):
    #проверка наличия пользователя в системе
    #user_chat_id = get_user_chat_id_from_system()

    if not user_chat_id:
        raise ValueError("Chat ID пользователя не указан")

    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{'7403382176:AAGe4SGM1aCnGDsyG_QXR7K210o3mWwDUzs'}/sendMessage"
    payload = {
        'chat_id': user_chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)

    if response.status_code != 200:
        raise Exception("Не удалось отправить сообщение в Telegram")
