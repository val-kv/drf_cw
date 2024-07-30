from rest_framework import serializers
from .models import Habit
import time
from django.utils import timezone


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        if data.get('related_habit') and data.get('reward'):
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть заполнены одновременно')
        return data

    def validate_related_habit(self, value):
        if value and self.initial_data.get('reward'):
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть заполнены одновременно')
        return value

    def validate_reward(self, value):
        if value and self.initial_data.get('related_habit'):
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть заполнены одновременно')
        return value

    def validate_habit_execution_time(self):
        start_time = time.time()
        self.initial_data['execution_time'] = start_time
        time.sleep(130)  # Симулируем длительное выполнение
        end_time = time.time()
        execution_time = end_time - start_time
        if execution_time > 120:
            raise serializers.ValidationError('Превышено ограничение времени выполнения привычки')
        return self

    def validate_related_pleasant_habit(self, value):
        if value and not value.pleasant:
            raise serializers.ValidationError('Для связанных привычек должно быть установлено значение True для флага "приятные".')
        return value

    def validate_reward_pleasant(self, data):
        if data.get('related_habit') and data.get('reward') and data.get('pleasant'):
            raise serializers.ValidationError('Приятные привычки не могут быть вознаграждением или связанной с ними привычкой')
        return data

    def validate_habit_days(self, data):
        habit = Habit.objects.get(pk=data.get('id'))
        last_performed = habit.last_performed
        if last_performed is not None:
            days_since_last_performed = (timezone.now() - last_performed).days
            if days_since_last_performed < 7:
                raise serializers.ValidationError('Эту привычку нельзя выполнять реже, чем раз в неделю')
            elif days_since_last_performed > 7:
                raise serializers.ValidationError('От привычки нельзя отказываться более чем на 7 дней')
        return data

