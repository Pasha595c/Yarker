from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register,
    registration_success,
    registration_success,
    EmailVerify,
    MyLoginView,
    profile,
    user_logout,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("register/", register, name="register"),
    path("registration-success/", registration_success, name="registration_success"),
    path(
        "verify_email/<uidb64>/<token>/",
        EmailVerify.as_view(),
        name="verify_email",
    ),
    path(
        "activation_failure/",
        TemplateView.as_view(template_name="activation_failure.html"),
        name="invalid_verify",
    ),
    path(
        "activation-success/",
        TemplateView.as_view(template_name="activation_success.html"),
        name="activation-success",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/reset_password.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/reset_password_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/reset_password_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("user_logout/", user_logout, name="user_logout"),
]
