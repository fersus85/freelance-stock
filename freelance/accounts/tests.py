from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    user_model = get_user_model()

    def test_create_user(self):
        user = self.user_model.objects.create_user(
            username='john',
            email='john@mail.ru',
            password='testpass123'
        )
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@mail.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = self.user_model.objects.create_superuser(
            username='superadmin',
            email='superadmin@mail.ru',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@mail.ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
