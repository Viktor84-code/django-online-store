from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.shortcuts import redirect


from .models import Contact, Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    contacts_data = Contact.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Сохраняем новый контакт в БД
        Contact.objects.create(name=name, phone=phone, message=message)

        # Обновляем список контактов после сохранения
        contacts_data = Contact.objects.all()

        return render(
            request,
            "catalog/contacts.html",
            {"message_sent": True, "name": name, "contacts": contacts_data},
        )

    return render(request, "catalog/contacts.html", {"contacts": contacts_data})


def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog/catalog.html", {"products": products})


def product_list(request):
    """Главная страница с динамическим списком товаров"""
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail(request, pk):
    """Детальная страница товара"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_create.html', {'form': form})