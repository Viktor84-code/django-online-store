from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


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


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "registration/profile_edit.html"
    success_url = "/"  # <--- просто корень

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registration/profile.html"
    context_object_name = "user_profile"

    def get_object(self, queryset=None):
        return self.request.user
