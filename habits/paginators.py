
from rest_framework import viewsets, request
from rest_framework.pagination import PageNumberPagination

from .models import Habit
from .serializers import HabitSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.filter(user=request.user)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
