from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .views import SignupPageView


class CustomUserTests(TestCase):
    def setUp(self):
        self.user = get_user_model()

    def test_create_user(self):
        user = self.user.objects.create_user(
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
        admin_user = self.user.objects.create_superuser(
            username='superadmin',
            email='superadmin@mail.ru',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@mail.ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,
                         SignupPageView.as_view().__name__)
