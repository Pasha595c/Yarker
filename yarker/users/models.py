from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _


# class Registration(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
class User(AbstractUser):
    """
    Индивидуальная модель пользователей,
    где электронная почта является уникальным идентификатором
    для аутентификации вместо имен пользователей.
    """

    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    email_verify = models.BooleanField(
        default=False, verbose_name="Подтверждённый Емаил"
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def str(self):
        return self.email
