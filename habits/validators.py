from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate_pleasant_habit(self, value):
        # Валидация: привычка должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Привычка должна быть публичной')
        return value

    def validate_linked_habit(self, value):
        # Валидация: связанной привычки должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Связанная привычка должна быть публичной')
        return value

    def validate_action(self, value):
        # Валидация: действие должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(action=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Действие уже используется для другой публичной привычки')
        return value

    def validate_place(self, value):
        # Валидация: место выполнения привычки должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(place=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Место выполнения уже используется для другой публичной привычки')
        return value

    def validate_reward(self, value):
        # Валидация: награда должна быть уникальной для каждой публичной привычки
        if Habit.objects.filter(reward=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Награда уже используется для другой публичной привычки')
        return value

    def validate_related_habit(self, value):
        # Валидация: связанной привычки должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Связанная привычка должна быть публичной')
        return value

    def validate_time_required(self, value):
        # Валидация: время выполнения привычки должно быть меньше 120 секунд
        if value > 120:
            raise serializers.ValidationError('Время выполнения не может превышать 120 секунд.')
        return value

    def validate_frequency(self, value):
        # Валидация: частота должна быть от 1 до 7
        if value < 1 or value > 7:
            raise serializers.ValidationError('Частота должна быть от 1 до 7.')
        return value

    def validate_is_pleasant(self, value):
        # Валидация: приятная привычка не может быть вознаграждением или связанной с ней привычкой
        if value and (self.instance.reward or self.instance.related_habit):
            raise serializers.ValidationError('Приятная привычка не может быть вознаграждением или связанной с ней привычкой.')
        return value

    def validate_periodicity(self, value):
        # Валидация: периодичность должна быть одной из возможных
        if value not in ('daily', 'weekly', 'monthly'):
            raise serializers.ValidationError('Периодичность должна быть одной из возможных')
        return value

    def validate(self, data):
        # Валидация: действие должно быть уникальным для каждой публичной привычки
        if self.instance and data.get('action') == self.instance.action:
            return data
        if Habit.objects.filter(action=data.get('action'), public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Действие уже используется для другой публичной привычки')
        return data