from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email="test@test.com", password="testpass123")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.check_password("testpass123"))

    def test_create_superuser(self):
        user = User.objects.create_superuser(email="admin@test.com", password="adminpass123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class UserRegistrationTest(TestCase):
    def test_register_page_status(self):
        response = self.client.get(reverse("users:register"))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(
            reverse("users:register"),
            {
                "email": "newuser@test.com",
                "phone": "1234567890",
                "country": "RU",
                "password1": "strongpass123",
                "password2": "strongpass123",
            },
        )
        self.assertEqual(response.status_code, 302)  # редирект после регистрации
        self.assertEqual(User.objects.count(), 1)


class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="login@test.com", password="loginpass123")

    def test_login_page_status(self):
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        response = self.client.post(reverse("users:login"), {"email": "login@test.com", "password": "loginpass123"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Вход")  # проверяем, что страница логина загрузилась

    def test_login_fail(self):
        response = self.client.post(reverse("users:login"), {"email": "login@test.com", "password": "wrongpass"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "errorlist")
