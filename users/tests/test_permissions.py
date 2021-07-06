import json
import os
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserAccessPermissionTestCase(APITestCase):

    def setUp(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'data.json')
        with open(file_path) as file:
            data = json.load(file)
        user_data = data.get('user_data')
        another_user_data = data.get('another_user_data')
        self.user = User.objects.create_user(**user_data)
        self.another_user = User.objects.create_user(**another_user_data)

    def test_object_level_permission(self):
        url = reverse('users:detail', args=[self.user.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        self.client.force_authenticate(user=self.another_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CreateOrAuthenticatedPermissionTestCase(APITestCase):

    def setUp(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'data.json')
        with open(file_path) as file:
            data = json.load(file)
        user_data = data.get('user_data')
        self.another_user_data = data.get('another_user_data')
        self.user = User.objects.create_user(**user_data)

    def test_create_permission(self):
        url = reverse('users:list')
        self.another_user_data['password2'] = self.another_user_data['password']
        response = self.client.post(url, self.another_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_permission(self):
        url = reverse('users:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



