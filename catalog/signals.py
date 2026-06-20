from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


@receiver(post_migrate)
def create_moderator_group(sender, **kwargs):
    if sender.name != 'catalog':
        return

    group, created = Group.objects.get_or_create(name='Модератор продуктов')

    if created:
        content_type = ContentType.objects.get_for_model(Product)

        # Право can_unpublish_product
        permission_unpublish = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type
        )

        # Право на удаление (существующее)
        permission_delete = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )

        group.permissions.add(permission_unpublish, permission_delete)
        group.save()
