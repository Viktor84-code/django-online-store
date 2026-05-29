from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse


from catalog.models import Category, Contact, Product


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        """Тест создания категории"""
        category = Category.objects.create(name="Электроника", description="Телефоны, ноутбуки, планшеты")
        self.assertEqual(str(category), "Электроника")
        self.assertEqual(category.name, "Электроника")

    def test_category_verbose_names(self):
        """Тест verbose_name полей категории"""
        category = Category.objects.create(name="Тест")
        self.assertEqual(category._meta.get_field("name").verbose_name, "Название")
        self.assertEqual(category._meta.get_field("description").verbose_name, "Описание")


class ProductModelTest(TestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.category = Category.objects.create(name="Электроника", description="Телефоны, ноутбуки")

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product.objects.create(
            name="iPhone 14", description="Смартфон Apple", price=799.99, category=self.category
        )
        self.assertEqual(str(product), "iPhone 14")
        self.assertEqual(product.price, 799.99)

    def test_product_foreign_key(self):
        """Тест связи продукта с категорией"""
        product = Product.objects.create(
            name="Samsung Galaxy S23", description="Смартфон Samsung", price=699.99, category=self.category
        )
        self.assertEqual(product.category.name, "Электроника")

    def test_product_price_positive(self):
        """Тест что цена положительная"""
        product = Product.objects.create(
            name="Футболка", description="Белая футболка", price=19.99, category=self.category
        )
        self.assertGreater(product.price, 0)


class ContactModelTest(TestCase):
    def test_contact_creation(self):
        """Тест создания контакта"""
        contact = Contact.objects.create(name="Иван Петров", phone="+7 999 123-45-67", message="Здравствуйте!")
        self.assertEqual(contact.name, "Иван Петров")
        self.assertEqual(contact.phone, "+7 999 123-45-67")
        self.assertEqual(contact.message, "Здравствуйте!")


class LoadDataCommandTest(TestCase):
    def test_load_test_data_command(self):
        """Тест кастомной команды load_test_data"""
        # Проверяем что в базе пусто
        self.assertEqual(Category.objects.count(), 0)
        self.assertEqual(Product.objects.count(), 0)

        # Выполняем команду
        call_command("load_test_data")

        # Проверяем что данные загрузились
        self.assertGreater(Category.objects.count(), 0)
        self.assertGreater(Product.objects.count(), 0)


class ViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Электроника", description="Телефоны, ноутбуки")
        self.product = Product.objects.create(
            name="iPhone 14", description="Смартфон Apple", price=799.99, category=self.category
        )

    def test_home_page(self):
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/home.html")

    def test_product_list_page(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/product_list.html")
        self.assertContains(response, "iPhone 14")

    def test_contacts_page_get(self):
        response = self.client.get(reverse('catalog:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/contacts.html")

    def test_contacts_page_post(self):
        response = self.client.post(
            reverse('catalog:contacts'),
            {"name": "Тестовый пользователь", "phone": "+7 999 123-45-67", "message": "Тестовое сообщение"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["message_sent"])
        self.assertEqual(response.context["name"], "Тестовый пользователь")
        self.assertEqual(Contact.objects.count(), 1)

    def test_product_detail_page(self):
        response = self.client.get(reverse('catalog:product_detail', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/product_detail.html")

    def test_product_create_page(self):
        response = self.client.get(reverse('catalog:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/product_create.html")
