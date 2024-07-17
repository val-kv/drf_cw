from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'action', 'creator', 'pleasant_habit', 'related_habit', 'periodicity', 'time_required', 'public', 'reward', 'linked_habit', 'execution_time')

    def validate(self, data):
        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and not data.get('reward'):
            raise serializers.ValidationError('Вы должны указать вознаграждение, если указана связанная привычка')
        return data

    def validate_pleasant_habit(self, value):
        # Валидация: привычка должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Привычка должна быть публичной')
        return value

    def validate_action(self, value):
        # Валидация: действие должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(action=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Действие уже используется для другой публичной привычки')
        return value

    def validate_execution_time(self, value):
        # Валидация: время выполнения должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(execution_time=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Время выполнения уже используется для другой публичной привычки')
        return value

    def validate_creator(self, value):
        # Валидация: создатель привычки должен быть публичный
        if value and not value.public:
            raise serializers.ValidationError('Создатель привычки должен быть публичный')
        return value

    def validate_place(self, value):
        # Валидация: место выполнения привычки должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(place=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Место выполнения уже используется для другой публичной привычки')
        return value

    def validate_linked_habit(self, value):
        # Валидация: связанной привычки должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Связанная привычка должна быть публичной')
        return value

    def validate_reward(self, value):
        # Валидация: вознаграждение должно быть уникальным для каждой публичной привычке
        if Habit.objects.filter(reward=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Вознаграждение уже используется для другой публичной привычки')
        return value

    def validate_periodicity(self, value):
        # Валидация: периодичность должна быть уникальным для каждой публичной привычки
        if Habit.objects.filter(periodicity=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Периодичность уже используется для другой публичной привычки')
        return value

    def validate_time_required(self, value):
        # Валидация: время выполнения должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(time_required=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Время выполнения уже используется для другой публичной привычки')
        return value

    def validate_time(self, value):
        # Валидация: время выполнения должно быть уникальным для каждой публичной привычки
        if Habit.objects.filter(time=value, public=True).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError('Время выполнения уже используется для другой публичной привычки')
        return value

    def validate_related_habit(self, value):
        # Валидация: связанной привычки должна быть публичной
        if value and not value.public:
            raise serializers.ValidationError('Связанная привычка должна быть публичной')
        return value

