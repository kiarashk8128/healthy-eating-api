from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import CustomUser, FamilyMember


class SignupTests(APITestCase):

    def test_signup_individual_user(self):
        url = reverse('signup')
        data = {
            "username": "johndoe",
            "password": "password123",
            "email": "johndoe@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1990-01-01",
            "gender": "male",
            "height": 175,
            "weight": 70,
            "is_family_head": False,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'johndoe')

    def test_signup_family_user(self):
        url = reverse('signup')
        data = {
            "username": "johnfamily",
            "password": "password123",
            "email": "johnfamily@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1980-05-15",
            "gender": "male",
            "height": 180,
            "weight": 80,
            "is_family_head": True,
            "family_members": [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "birthday": "2005-07-20",
                    "gender": "female",
                    "height": 160,
                    "weight": 55
                },
                {
                    "first_name": "Jimmy",
                    "last_name": "Doe",
                    "birthday": "2010-08-25",
                    "gender": "male",
                    "height": 140,
                    "weight": 40
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(FamilyMember.objects.count(), 2)
        self.assertEqual(CustomUser.objects.get().username, 'johnfamily')

    def test_signup_missing_fields(self):
        url = reverse('signup')
        data = {
            "username": "janedoe",
            "password": "password123",
            # Missing email, first_name, last_name, etc.
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_signup_invalid_email(self):
        url = reverse('signup')
        data = {
            "username": "invalidemail",
            "password": "password123",
            "email": "not-an-email",
            "first_name": "Jane",
            "last_name": "Doe",
            "birthday": "1990-01-01",
            "gender": "female",
            "height": 160,
            "weight": 60,
            "is_family_head": False,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_signup_duplicate_username(self):
        url = reverse('signup')
        data = {
            "username": "johndoe",
            "password": "password123",
            "email": "johndoe1@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1990-01-01",
            "gender": "male",
            "height": 175,
            "weight": 70,
            "is_family_head": False,
        }
        self.client.post(url, data, format='json')
        data['email'] = 'johndoe2@example.com'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)
