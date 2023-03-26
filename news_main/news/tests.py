from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# have to has passwords, can't directly name them in tests apparently
class UserModelTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        password = 'password123'
        hashed_password = make_password(password)
        user = User.objects.create(
            email='user@example.com',
            password= hashed_password,
            first_name='big',
            last_name='bill',
        )
        self.assertEqual(user.email, 'user@example.com')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.first_name, 'big')
        self.assertEqual(user.last_name, 'bill')
