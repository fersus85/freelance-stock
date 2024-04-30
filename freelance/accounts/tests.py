from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .views import (
    SignupPageView,
    UserProfile,
    FreelanOfficeView,
    CustomerOfficeView)


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
        self.assertContains(self.response, 'Регистрация')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,
                         SignupPageView.as_view().__name__)


class ProfilePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='john',
            email='john@mail.ru',
            password='testpass123'
        )
        self.client.login(username='john', password='testpass123')
        url = reverse('profile', args=[self.user.pk,])
        self.response = self.client.get(url)

    def test_profile_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'profile.html')
        self.assertContains(self.response, 'Профиль')

    def test_profile_view(self):
        view = resolve(f'/accounts/profile/{self.user.pk}/')
        self.assertEqual(view.func.__name__,
                         UserProfile.as_view().__name__)


class OfficeFreelPageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='john',
            email='john@mail.ru',
            password='testpass123',
            is_freelancer=True
        )
        self.client.login(username='john', password='testpass123')
        url = reverse('f_office', args=[self.user.pk,])
        self.response = self.client.get(url)

    def test_office_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'freelance_office.html')
        self.assertContains(self.response, 'Личный')

    def test_office_view(self):
        view = resolve(f'/accounts/f_office/{self.user.pk}/')
        self.assertEqual(view.func.__name__,
                         FreelanOfficeView.as_view().__name__)


class OfficeCustPageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='john',
            email='john@mail.ru',
            password='testpass123',
            is_freelancer=False
        )
        self.client.login(username='john', password='testpass123')
        url = reverse('c_office', args=[self.user.pk,])
        self.response = self.client.get(url)

    def test_office_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'customer_office.html')
        self.assertContains(self.response, 'Личный')

    def test_office_view(self):
        view = resolve(f'/accounts/c_office/{self.user.pk}/')
        self.assertEqual(view.func.__name__,
                         CustomerOfficeView.as_view().__name__)
