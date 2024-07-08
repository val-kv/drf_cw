from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'action', 'creator', 'pleasant_habit', 'public', 'reward', 'linked_habit', 'execution_time')

    def validate(self, data):
        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: времени выполнения привычки
        if data.get('execution_time') > 120:
            raise serializers.ValidationError("Время выполнения привычки не может быть более 120 секунд")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        # Валидация: связанной привычки и вознаграждения
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нет возможности одновременного выбора связанной привычки и указания вознаграждения")

        return data
