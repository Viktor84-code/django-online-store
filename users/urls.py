from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomAuthenticationForm
from .views import ProfileView
from .views import RegisterView, ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=CustomAuthenticationForm
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
