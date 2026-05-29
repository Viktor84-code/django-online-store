from django.test import TestCase
from django.urls import reverse

from blog.models import BlogPost


class BlogModelTest(TestCase):
    def test_blog_post_creation(self):
        post = BlogPost.objects.create(title="Тестовая статья", content="Текст статьи", is_published=True)
        self.assertEqual(str(post), "Тестовая статья")
        self.assertEqual(post.views_count, 0)


class BlogViewsTest(TestCase):
    def setUp(self):
        self.published_post = BlogPost.objects.create(title="Опубликованная статья", content="Текст", is_published=True)
        self.unpublished_post = BlogPost.objects.create(title="Черновик", content="Текст", is_published=False)

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
        response = self.client.get(reverse("blog:create"))
        self.assertEqual(response.status_code, 200)

    def test_blog_edit_page(self):
        response = self.client.get(reverse("blog:update", args=[self.published_post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_blog_delete_page(self):
        response = self.client.get(reverse("blog:delete", args=[self.published_post.pk]))
        self.assertEqual(response.status_code, 200)
