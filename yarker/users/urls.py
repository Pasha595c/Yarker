from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    RegisterView,
    # registration_success,
    EmailVerifyView,
    MyLoginView,
    user_logoutView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "login/",
        MyLoginView.as_view(template_name="users/login/login.html"),
        name="login",
    ),
    path("register/", RegisterView, name="register"),
    path(
        "registration-success/",
        MyLoginView.as_view(
            template_name="users/registration/registration_success.html"
        ),
        name="registration_success",
    ),
    path(
        "verify_email/<uidb64>/<token>/",
        EmailVerifyView.as_view(),
        name="verify_email",
    ),
    path(
        "activation_failure/",
        TemplateView.as_view(template_name="users/login/activation_failure.html"),
        name="invalid_verify",
    ),
    path(
        "activation-success/",
        TemplateView.as_view(template_name="users/login/activation_success.html"),
        name="activation-success",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/reset_password/reset_password.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/reset_password/reset_password_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/reset_password/reset_password_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/reset_password/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("user_logout/", user_logoutView, name="user_logout"),
]
