from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class AccountTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('users:register')
        data = {
            "username": "Kermani",
            "password": "mK@1369!",
            "retype_password": "mK@1369!",
            "email": "me@kermani.com",
            "first_name": "MEYSAM",
            "last_name": "KERMANI",
            "user_type": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username="Kermani").email, 'me@kermani.com')