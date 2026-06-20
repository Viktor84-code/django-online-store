from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = 'Create moderator group and assign permissions'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        if created:
            content_type = ContentType.objects.get_for_model(Product)

            permissions = Permission.objects.filter(
                content_type=content_type,
                codename__in=['can_unpublish_product', 'delete_product']
            )

            group.permissions.set(permissions)
            group.save()

            self.stdout.write(self.style.SUCCESS('Group "Модератор продуктов" created with permissions'))
        else:
            self.stdout.write(self.style.WARNING('Group already exists'))
