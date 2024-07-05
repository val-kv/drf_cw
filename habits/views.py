from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import HabitForm
from .models import Habit


class HabitCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = HabitForm
    model = Habit

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('habit-list')


class HabitUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = HabitForm
    model = Habit

    def get_success_url(self):
        return reverse('habit-list')


class HabitDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Habit

    def get_success_url(self):
        return reverse('habit-list')


@login_required
def habit_list(request):
    habits = Habit.objects.filter(creator=request.user)
    return render(request, 'habits/habit_list.html', {'habits': habits})


def public_habit_list(request):
    habits = Habit.objects.filter(public=True)
    return render(request, 'habits/public_habit_list.html', {'habits': habits})


def register(request):
    if request.method == 'POST':
        # Handle registration logic
        return HttpResponseRedirect('/')
    else:
        # Render registration form
        return render(request, 'habits/register.html')


def login(request):
    if request.method == 'POST':
        # Handle login logic
        return HttpResponseRedirect('/')
    else:
        # Render login form
        return render(request, 'habits/login.html')
