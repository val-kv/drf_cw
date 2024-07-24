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