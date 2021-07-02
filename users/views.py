from rest_framework import generics, mixins
from users.models import CustomUser
from users.permissions import UserAccessPermission
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserDetailSerializer
)


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        if self.request.method == 'POST':
            return UserCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [UserAccessPermission]
