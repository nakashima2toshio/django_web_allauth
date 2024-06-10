# accounts/tests/test_models.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import logging

"""
1. userの登録 post - user@email.com/ password
2. login
3. logout
4. userの削除 
"""
logger = logging.getLogger(__name__)
CustomUser = get_user_model()


# class CustomUser のテスト

class TestCustomUser(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'user@email.com',
            'username': 'testuser',
            'password': 'testpassword123',
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        logger.info('accounts/models.py -- setUp ----')

    def test_user_creation(self):
        user = CustomUser.objects.get(email=self.user_data['email'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.username, self.user_data['username'])
        self.assertTrue(user.check_password(self.user_data['password']))
        logger.info('accounts/models.py -- test_user_creation ----')

    def test_login(self):
        login = self.client.login(email='user@email.com', password='testpassword123')
        logger.info('accounts/models.py -- login ----')
        self.assertTrue(login)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(email='user@email.com', password='testpassword123')
        logger.info('accounts/models.py -- login ----')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Check redirect after logout

    def tearDown(self):
        logger.info('accounts/models.py -- tear-down ----')

# python manage.py makemigrations
# python manage.py migrate
# python manage.py test accounts.tests.test_models
