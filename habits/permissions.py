from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, DeleteView

from habits.models import Habit


class HabitDetailView(UserPassesTestMixin, DetailView):
    model = Habit

    def test_func(self):
        habit = self.get_object()
        return self.request.user == habit.creator or self.request.user.has_perm('app_name.can_edit_habit')


class HabitUpdateView(UserPassesTestMixin, UpdateView):
    model = Habit

    def test_func(self):
        habit = self.get_object()
        return self.request.user == habit.creator or self.request.user.has_perm('app_name.can_edit_habit')


class HabitDeleteView(UserPassesTestMixin, DeleteView):
    model = Habit

    def test_func(self):
        habit = self.get_object()
        return self.request.user == habit.creator or self.request.user.has_perm('app_name.can_delete_habit')