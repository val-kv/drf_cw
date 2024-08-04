from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Habit
from .serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class HabitListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(creator=self.request.user)


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)