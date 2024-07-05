from django.core.exceptions import ValidationError


class UniqueRelatedRewardValidator:
    def validate(self, habit):
        if habit.related_habit is not None and habit.reward != '':
            raise ValidationError('Cannot have both related habit and reward at the same time.')


class UniqueRewardRelatedHabitValidator:
    def validate(self, related_habit):
        if related_habit.habit.reward != '' and related_habit.habit.related_habit is not None:
            raise ValidationError('Cannot have both reward and related habit at the same time.')


class MaxTimeValidator:
    def validate(self, habit):
        if habit.time_required.total_seconds() > 120:
            raise ValidationError('Time required for habit cannot be more than 120 seconds.')


class PleasantHabitRelatedHabitValidator:
    def validate(self, related_habit):
        if not related_habit.habit.pleasant_habit:
            raise ValidationError('Related habit must be a pleasant habit.')


class PleasantHabitValidator:
    def validate(self, habit):
        if habit.pleasant_habit and (habit.reward != '' or habit.related_habit is not None):
            raise ValidationError('Pleasant habit cannot have reward or related habit.')


class MinPeriodicityValidator:
    def validate(self, habit):
        if habit.periodicity != 'daily' and habit.periodicity != 'weekly':
            raise ValidationError('Habit must be performed at least once a week.')


class MaxGapPeriodicityValidator:
    def validate(self, habit):
        last_habit = habit.creator.habits.filter(
            pleasant_habit=habit.pleasant_habit,
            place=habit.place,
            time=habit.time
        ).order_by('-id').first()

        if last_habit and (habit.periodicity - last_habit.periodicity).days > 7:
            raise ValidationError('Habit cannot be skipped for more than 7 days.')
