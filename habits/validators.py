import datetime
from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate_related_habit(self, value):
        if value and self.initial_data.get('reward'):
            raise serializers.ValidationError('Связанная привычка и вознаграждение не могут быть заполнены одновременно')
        return value

    def validate_time_required(self, value):
        if value > datetime.timedelta(minutes=2):
            raise serializers.ValidationError('Время выполнения не может быть более 120 секунд')
        return value

    def validate_related_habit_2(self, value):
        if value and not value.pleasant_habit:
            raise serializers.ValidationError('Связанная привычка может быть только приятной')
        return value

    def validate_pleasant_habit(self, value):
        if (value and self.initial_data.get('reward')) or (value and self.initial_data.get('related_habit')):
            raise serializers.ValidationError('У приятной привычки не может быть награды или связанной привычки')
        return value

    def validate_periodicity(self, value):
        if value not in ['daily', 'once a week', 'twice a week', '3 times a week', '4 times a week']:
            raise serializers.ValidationError('Привычка не может выполняться реже чем раз в 7 дней')
        return value
