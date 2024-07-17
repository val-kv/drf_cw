from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Habit


class HabitTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='12345')

        # Create a test habit
        Habit.objects.create(user=test_user, name='Exercise', description='Daily exercise habit')

    def test_habit_creator(self):
        habit = Habit.objects.get(id=1)
        expected_creator = f'{habit.creator}'
        self.assertEqual(expected_creator, 'testuser')

    def test_habit_list_view(self):
        client = APIClient()
        response = client.get('/habits/')
        self.assertEqual(response.status_code, 200)

    def test_habit_detail_view(self):
        client = APIClient()
        response = client.get('/habits/1/')  # Assuming habit with id=1 exists
        self.assertEqual(response.status_code, 200)

    def test_habit_create_view(self):
        client = APIClient()
        response = client.post('/habits/', data={'name': 'New Habit', 'description': 'New habit description'})
        self.assertEqual(response.status_code, 201)