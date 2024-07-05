from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Habit Tracker API",
        default_version='v1',
        description="Habit Tracker API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

app_name = 'habit_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('habit/create/', views.HabitCreateView.as_view(), name='habit-create'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit-update'),
    path('habit/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit-delete'),
    path('habit/list/', views.habit_list, name='habit-list'),
    path('habit/public/', views.public_habit_list, name='public-habit-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]