from django.urls import path, include
from rest_framework import routers

from .views import UserCreateView, UserLoginView, UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]