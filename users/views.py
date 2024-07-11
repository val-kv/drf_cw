from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password', None)
        instance = serializer.save()
        if password:
            instance.set_password(password)
            instance.save()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    