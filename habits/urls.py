from django.urls import path, include
from rest_framework import permissions, routers
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import HabitCreateView, HabitUpdateView, HabitDeleteView, HabitListView, HabitDetailView, \
    PublicHabitViewSet, HabitViewSet

app_name = 'habits'

schema_view = get_schema_view(
    openapi.Info(
        title="Habit Tracker API",
        default_version='v1',
        description="Habit Tracker API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'user-habits', HabitViewSet, basename='user-habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habits')

urlpatterns = [
    path('create/', HabitCreateView.as_view(), name='habit-create'),
    path('<int:pk>/update/', HabitUpdateView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDeleteView.as_view(), name='habit-delete'),
    path('', HabitListView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('api/', include(router.urls)),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
