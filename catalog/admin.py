from django.contrib import admin

from .models import Category, Contact, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "created_at", "updated_at"]
    list_filter = ["category", "created_at", "price"]
    search_fields = ["name", "description"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]
