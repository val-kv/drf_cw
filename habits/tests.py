import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import User, Habit


class HabitTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=f'testuser_{uuid.uuid4().hex[:8]}',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_habit(self):
        url = reverse("habits:habit-list")
        data = {'name': 'Test Habit'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().name, 'Test Habit')

    def test_get_habit(self):
        habit = Habit.objects.create(name='Test Habit', creator=self.user)
        url = reverse("habits:habit-detail", args=[habit.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, habit.name)

    def test_update_habit(self):
        habit = Habit.objects.create(name='Test Habit', creator=self.user)
        url = reverse("habits:habit-detail", args=[habit.id])
        data = {'username': 'Updated Habit'}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.name, 'Updated Habit')

    def test_partial_update_habit(self):
        habit = Habit.objects.create(name='Test Habit', creator=self.user)
        url = reverse("habits:habit-detail", args=[habit.id])
        data = {'name': 'Partially Updated Habit'}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.name, 'Partially Updated Habit')

    def test_delete_habit(self):
        habit = Habit.objects.create(name='Test Habit', creator=self.user)
        url = reverse("habits:habit-detail", args=[habit.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_public_habit_viewset(self):
        public_habit = Habit.objects.create(name='Public Habit', creator=self.user, public=True)
        url = reverse("habits:public-habit")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, public_habit.name)

    def test_owner_permission(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        other_habit = Habit.objects.create(name='Other Habit', creator=other_user)

        url = reverse("habits:habit-detail", args=[other_habit.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_send_telegram_message(self):
        url = reverse("habits:send_telegram_message")
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
