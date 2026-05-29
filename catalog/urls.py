from django.urls import path
from catalog import views

app_name = "catalog"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("catalog/", views.ProductListView.as_view(), name="product_list"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("catalog/product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("create/", views.ProductCreateView.as_view(), name="product_create"),
]
