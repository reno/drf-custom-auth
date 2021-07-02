from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from users.permissions import UserAccessPermission
from users.serializers import (
    UserListSerializer, UserCreateSerializer, UserDetailSerializer
)
from users.tokens import email_confirmation_token


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


class EmailConfirmView(APIView):

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            user = None
        if user and email_confirmation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return Response(
                {'Message': 'Email confirmed with success.'},
                status=201
            )
        else:
            return Response(
                {'Error': 'The email confirmation link was invalid.'},
                status=400
            )
