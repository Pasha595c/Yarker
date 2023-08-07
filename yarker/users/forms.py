from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordResetForm,
    AuthenticationForm as DjangoAuthenticationForm,
)
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from users.utils import send_email_for_verify

User = get_user_model()


class UserCreationForm(UserCreationForm):
    """Форма регистрации User"""

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)


class CustomUserCreationForm(UserCreationForm):
    """Форма создания модели User"""

    class Meta(UserCreationForm):
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """Форма изменения модели User"""

    class Meta:
        model = User
        fields = ("email",)


class AuthenticationForm(DjangoAuthenticationForm):
    """Форма авторизации User"""

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    "Почта не подтверждена, проверьте свой Email",
                    code="invalid_login",
                )

        return self.cleaned_data
