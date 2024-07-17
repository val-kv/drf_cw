from django.urls import reverse
from rest_framework.test import APITestCase

from users.models import User


class UserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_list_api(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_user_detail_api(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_user_create_api(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'newuser')

    def test_user_update_api(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {'username': 'updateduser'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'updateduser')

    def test_user_delete_api(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)