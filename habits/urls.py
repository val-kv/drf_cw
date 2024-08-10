from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import PublicHabitViewSet, HabitViewSet, HabitListView, HabitDetailView


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
router.register(r'habits', HabitViewSet, basename='habits')
router.register(r'public-habits', PublicHabitViewSet, basename='public-habits')

urlpatterns = [
    path('create/', HabitViewSet.create, name='habit-create'),
    path('<int:pk>/update/', HabitViewSet.update, name='habit-update'),
    path('<int:pk>/delete/', HabitViewSet.destroy, name='habit-delete'),
    path('', HabitListView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('api/', include(router.urls)),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('send-telegram-message/', HabitViewSet.as_view({'post': 'send_telegram_message'}), name='send_telegram_message'),
    path('', include(router.urls)),
]
