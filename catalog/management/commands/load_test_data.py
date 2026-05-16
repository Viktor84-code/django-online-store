from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        # Очищаем существующие данные
        self.stdout.write('Очистка существующих данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем фикстуры
        self.stdout.write('Загрузка категорий...')
        call_command('loaddata', 'fixtures/categories.json')

        self.stdout.write('Загрузка продуктов...')
        call_command('loaddata', 'fixtures/products.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))
