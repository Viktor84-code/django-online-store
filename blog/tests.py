from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from blog.models import BlogPost

User = get_user_model()


class BlogModelTest(TestCase):
    def test_blog_post_creation(self):
        post = BlogPost.objects.create(title="Тестовая статья", content="Текст статьи", is_published=True)
        self.assertEqual(str(post), "Тестовая статья")
        self.assertEqual(post.views_count, 0)


class BlogViewsTest(TestCase):
    def setUp(self):
        self.published_post = BlogPost.objects.create(title="Опубликованная статья", content="Текст", is_published=True)
        self.unpublished_post = BlogPost.objects.create(title="Черновик", content="Текст", is_published=False)
        group, created = Group.objects.get_or_create(name='Контент-менеджер')
        if created:
            from django.contrib.contenttypes.models import ContentType
            from django.contrib.auth.models import Permission
            content_type = ContentType.objects.get_for_model(BlogPost)
            permissions = Permission.objects.filter(content_type=content_type)
            group.permissions.set(permissions)
            group.save()

    def test_blog_list_shows_only_published(self):
        response = self.client.get(reverse("blog:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Опубликованная статья")
        self.assertNotContains(response, "Черновик")

    def test_blog_detail_page(self):
        response = self.client.get(reverse("blog:detail", args=[self.published_post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_views_count_increments(self):
        self.assertEqual(self.published_post.views_count, 0)
        self.client.get(reverse("blog:detail", args=[self.published_post.pk]))
        self.published_post.refresh_from_db()
        self.assertEqual(self.published_post.views_count, 1)

    def test_unpublished_post_404(self):
        response = self.client.get(reverse("blog:detail", args=[self.unpublished_post.pk]))
        self.assertEqual(response.status_code, 404)

    def test_blog_create_page(self):
        User.objects.create_user(email="test@test.com", password="testpass123")
        self.client.login(email="test@test.com", password="testpass123")
        response = self.client.get("/blog/create/")
        self.assertEqual(response.status_code, 200)

    def test_blog_edit_page(self):
        # Обычный пользователь - доступ запрещен
        user = User.objects.create_user(email="test@test.com", password="testpass123")
        self.client.login(email="test@test.com", password="testpass123")
        response = self.client.get(f"/blog/{self.published_post.pk}/update/")
        self.assertEqual(response.status_code, 403)

        # Контент-менеджер - доступ разрешен
        manager = User.objects.create_user(email="manager@test.com", password="testpass123")
        group = Group.objects.get(name='Контент-менеджер')
        manager.groups.add(group)
        self.client.login(email="manager@test.com", password="testpass123")
        response = self.client.get(f"/blog/{self.published_post.pk}/update/")
        self.assertEqual(response.status_code, 200)

    def test_blog_delete_page(self):
        # Обычный пользователь - доступ запрещен
        user = User.objects.create_user(email="test@test.com", password="testpass123")
        self.client.login(email="test@test.com", password="testpass123")
        response = self.client.get(f"/blog/{self.published_post.pk}/delete/")
        self.assertEqual(response.status_code, 403)

        # Контент-менеджер - доступ разрешен
        manager = User.objects.create_user(email="manager@test.com", password="testpass123")
        group = Group.objects.get(name='Контент-менеджер')
        manager.groups.add(group)
        self.client.login(email="manager@test.com", password="testpass123")
        response = self.client.get(f"/blog/{self.published_post.pk}/delete/")
        self.assertEqual(response.status_code, 200)


class ContentManagerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@test.com',
            password='testpass123'
        )
        self.manager = User.objects.create_user(
            email='manager@test.com',
            password='testpass123'
        )
        self.post = BlogPost.objects.create(
            title='Test Post',
            content='Test content'
        )

        # Создаем группу контент-менеджеров
        group, _ = Group.objects.get_or_create(name='Контент-менеджер')
        content_type = ContentType.objects.get_for_model(BlogPost)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)
        self.manager.groups.add(group)

    def test_manager_can_edit(self):
        self.client.login(email='manager@test.com', password='testpass123')
        response = self.client.get(reverse('blog:update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_regular_user_cannot_edit(self):
        self.client.login(email='user@test.com', password='testpass123')
        response = self.client.get(reverse('blog:update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)

    def test_manager_can_delete(self):
        self.client.login(email='manager@test.com', password='testpass123')
        response = self.client.get(reverse('blog:delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_regular_user_cannot_delete(self):
        self.client.login(email='user@test.com', password='testpass123')
        response = self.client.get(reverse('blog:delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)
