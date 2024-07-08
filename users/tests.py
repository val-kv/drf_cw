from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_list_api(self):
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_detail_api(self):
        url = f'/api/users/{self.user.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_create_api(self):
        url = '/api/users/'
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_update_api(self):
        url = f'/api/users/{self.user.id}/'
        data = {'username': 'updateduser'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_user_delete_api(self):
        url = f'/api/users/{self.user.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
