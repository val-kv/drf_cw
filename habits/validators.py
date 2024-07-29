from rest_framework.serializers import ValidationError

from habits.models import Habit


def validate_frequency(value):
    # Валидация: частота должна быть от 1 до 7
    if value < 1 or value > 7:
        raise ValidationError('Частота должна быть от 1 до 7.')
    return value


def validate_time_required(value):
    # Валидация: время выполнения привычки должно быть меньше 120 секунд
    if value > 120:
        raise ValidationError('Время выполнения не может превышать 120 секунд.')
    return value


def validate_periodicity(value):
    # Валидация: периодичность должна быть одной из возможных
    if value not in ('daily', 'weekly', 'monthly'):
        raise ValidationError('Периодичность должна быть одной из возможных')
    return value


def validate_pleasant_habit(value):
    # Валидация: привычка должна быть публичной
    if value and not value.public:
        raise ValidationError('Привычка должна быть публичной')
    return value


def validate_linked_habit(value):
    # Валидация: связанной привычки должна быть публичной
    if value and not value.public:
        raise ValidationError('Связанная привычка должна быть публичной')
    return value


def validate_related_habit(value):
    # Валидация: связанной привычки должна быть публичной
    if value and not value.public:
        raise ValidationError('Связанная привычка должна быть публичной')
    return value


def validate_reward(value, self=None):
    # Валидация: награда должна быть уникальной для каждой публичной привычки
    if Habit.objects.filter(reward=value, public=True).exclude(id=self.instance.id).exists():
        raise ValidationError('Награда уже используется для другой публичной привычки')
    return value


def validate_action(value, self=None):
    # Валидация: действие должно быть уникальным для каждой публичной привычки
    if Habit.objects.filter(action=value, public=True).exclude(id=self.instance.id).exists():
        raise ValidationError('Действие уже используется для другой публичной привычки')
    return value


def validate_place(value, self=None):
    # Валидация: место выполнения привычки должно быть уникальным для каждой публичной привычки
    if Habit.objects.filter(place=value, public=True).exclude(id=self.instance.id).exists():
        raise ValidationError('Место выполнения уже используется для другой публичной привычки')
    return value


def validate(value, self=None):
    # Валидация: действие должно быть уникальным для каждой публичной привычки
    if Habit.objects.filter(action=value, public=True).exclude(id=self.instance.id).exists():
        raise ValidationError('Действие уже используется для другой публичной привычки')
    return value
