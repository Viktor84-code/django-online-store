from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from blog.models import BlogPost


class Command(BaseCommand):
    help = "Create content manager group and assign permissions"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Контент-менеджер")

        if created:
            content_type = ContentType.objects.get_for_model(BlogPost)

            # Все права на блог (add, change, delete, view)
            permissions = Permission.objects.filter(content_type=content_type)

            group.permissions.set(permissions)
            group.save()

            self.stdout.write(self.style.SUCCESS('Group "Контент-менеджер" created with all blog permissions'))
        else:
            self.stdout.write(self.style.WARNING("Group already exists"))
