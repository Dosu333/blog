from django.contrib.auth import get_user_model

from rest_framework import generics, permissions

from .serializers import UserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated)

    def get_object(self):
        return self.request.user