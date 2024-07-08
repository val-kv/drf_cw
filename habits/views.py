from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets, request
from rest_framework.exceptions import PermissionDenied

from .forms import HabitForm
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated


class HabitCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = HabitForm
    model = Habit

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('habit-detail', kwargs={'pk': self.object.pk})


class HabitUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = HabitForm
    model = Habit

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('habit-detail', kwargs={'pk': self.object.pk})


class HabitDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Habit

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('habit-list')


class HabitListView(LoginRequiredMixin, generic.ListView):
    model = Habit

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitDetailView(LoginRequiredMixin, generic.DetailView):
    model = Habit

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def send_telegram_message(self, request, *args, **kwargs):
        # Проверяем, что пользователь авторизован
        if not request.user.is_authenticated:
            raise PermissionDenied("Пользователь не авторизован")
