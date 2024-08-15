from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import CustomUser


class LoginTests(APITestCase):

    def setUp(self):
        # Create a user to test login
        self.user = CustomUser.objects.create_user(
            username="johndoe",
            password="password123",
            email="johndoe@example.com"
        )

    def test_login_with_valid_credentials(self):
        url = reverse('login')
        data = {
            "username": "johndoe",
            "password": "password123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_with_invalid_credentials(self):
        url = reverse('login')
        data = {
            "username": "johndoe",
            "password": "wrongpassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_missing_fields(self):
        url = reverse('login')
        data = {
            "username": "johndoe",
            # Missing password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
