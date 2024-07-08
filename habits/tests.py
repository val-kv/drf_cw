from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Habit


class HabitTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        test_user = User.objects.create_user(username='testuser', password='12345')

        # Создаем тестовую привычку
        Habit.objects.create(user=test_user, name='Exercise', description='Daily exercise habit')

    def test_habit_creator(self):
        habit = Habit.objects.get(id=1)
        expected_creator = f'{habit.creator}'
        self.assertEqual(expected_creator, 'testuser')

    def test_habit_action(self):
        habit = Habit.objects.get(id=1)
        expected_action = f'{habit.action}'
        self.assertEqual(expected_action, 'Exercise')

    def test_user_habits_count(self):
        user = User.objects.get(username='testuser')
        habits_count = Habit.objects.filter(user=user).count()
        self.assertEqual(habits_count, 1)


class HabitViewSetTests(TestCase):
    def test_habit_list_view(self):
        client = APIClient()
        response = client.get('/habits/')
        self.assertEqual(response.status_code, 200)

    def test_habit_detail_view(self):
        habit = Habit.objects.create(name='Exercise', description='Daily exercise habit')
        client = APIClient()
        response = client.get(f'/habits/{habit.id}/')
        self.assertEqual(response.status_code, 200)

    def test_habit_create_view(self):
        client = APIClient()
        response = client.post('/habits/', data={'name': 'Exercise', 'description': 'Daily exercise habit'})
        self.assertEqual(response.status_code, 201)


class TelegramIntegrationTests(TestCase):
    def test_send_telegram_message_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/send_telegram_message/', data={'message': 'Test message'})
        self.assertEqual(response.status_code, 200)

    def test_send_telegram_message_unauthenticated_user(self):
        client = APIClient()
        response = client.post('/send_telegram_message/', data={'message': 'Test message'})
        self.assertEqual(response.status_code, 401)