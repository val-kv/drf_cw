from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from users.models import User
from .models import Habit


class HabitListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_habits_list(self):
        habit = Habit.objects.create(creator=self.user, action='Test Habit')
        response = self.client.get(reverse('habit-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        habits = response.data
        self.assertEqual(len(habits), 1)
        self.assertEqual(habits[0]['action'], 'Test Habit')

    def test_get_habits_list_unauthenticated(self):
        response = self.client.get(reverse('habit-list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class HabitDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_habit_detail(self):
        habit = Habit.objects.create(creator=self.user, action='Test Habit')

        response = self.client.get(reverse('habit-detail', kwargs={'pk': habit.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        habit_data = response.data
        self.assertEqual(habit_data['action'], 'Test Habit')

    def test_get_habit_detail_unauthenticated(self):

        habit = Habit.objects.create(creator=self.user, action='Test Habit')

        response = self.client.get(reverse('habit-detail', kwargs={'pk': habit.pk}))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_habit_detail(self):
        habit = Habit.objects.create(creator=self.user, action='Test Habit')

        data = {'action': 'Updated Habit'}
        response = self.client.patch(reverse('habit-detail', kwargs={'pk': habit.pk}), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        habit.refresh_from_db()
        self.assertEqual(habit.action, 'Updated Habit')

    def test_delete_habit_detail(self):
        habit = Habit.objects.create(creator=self.user, action='Test Habit')
        response = self.client.delete(reverse('habit-detail', kwargs={'pk': habit.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
