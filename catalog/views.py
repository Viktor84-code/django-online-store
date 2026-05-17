from django.shortcuts import render

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
