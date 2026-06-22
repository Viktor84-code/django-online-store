from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/", blank=True, null=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    congratulation_sent = models.BooleanField(default=False, verbose_name="Поздравление отправлено")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts',
        verbose_name='Владелец'
    )

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-created_at"]
        permissions = [
            ('can_manage_blog', 'Может управлять блогом'),
        ]

    def __str__(self):
        return self.title
