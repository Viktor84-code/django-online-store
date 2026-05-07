from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Здесь можно добавить логирование или отправку email

        return render(request, 'catalog/contacts.html', {
            'message_sent': True,
            'name': name
        })

    return render(request, 'catalog/contacts.html')
