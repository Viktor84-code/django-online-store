from django.urls import path

from catalog import views

from .views import products_by_category

app_name = "catalog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("catalog/", views.ProductListView.as_view(), name="product_list"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("catalog/product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("category/<int:category_id>/", products_by_category, name="products_by_category"),
]
