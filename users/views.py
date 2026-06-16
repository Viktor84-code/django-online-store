from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис!"
        message = "Спасибо за регистрацию. Мы рады вас видеть!"
        send_mail(
            subject,
            message,
            "viktor.britkin84@yandex.ru",
            [user_email],
            fail_silently=False,
        )