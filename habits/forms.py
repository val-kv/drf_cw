from django import forms
from .models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['action', 'creator', 'pleasant_habit', 'public']  # Specify the fields you want to include in the form


class HabitCreateForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['action', 'creator', 'pleasant_habit', 'public']  # Specify the fields you want to include in the form
        exclude = ['id', 'creator', 'created_at', 'updated_at']  # Exclude any fields you don't want to include
