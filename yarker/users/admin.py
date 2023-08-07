from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from django.db import models

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    """Класс отображения в админке модели User"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "email",
        "email_verify",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Права", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "20"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 2, "cols": 25})},
    }


admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "Администрирование сайта Ярметиз"
admin.site.index_title = "Настройки"
