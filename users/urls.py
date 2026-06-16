from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomAuthenticationForm
from .views import RegisterView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=CustomAuthenticationForm
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
