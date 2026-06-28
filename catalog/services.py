from django.core.cache import cache

from .models import Product


def get_products_by_category(category_id):
    """Возвращает список опубликованных продуктов в указанной категории."""
    return Product.objects.filter(category_id=category_id, is_published=True)


def get_cached_products_by_category(category_id):
    """Возвращает список продуктов из кэша или из БД с сохранением в кэш."""
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = get_products_by_category(category_id)
        cache.set(cache_key, products, 60 * 15)  # TTL 15 минут

    return products
