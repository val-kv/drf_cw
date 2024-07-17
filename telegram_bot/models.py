from django.db import models


class TelegramBot(models.Model):
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Reminder(models.Model):
    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=255)
    message = models.TextField()
