from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

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
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        habit = self.get_object()
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def send_telegram_message(self, request, *args, **kwargs):
        # Проверяем, что пользователь авторизован
        if not request.user.is_authenticated:
            raise PermissionDenied("Пользователь не авторизован")
