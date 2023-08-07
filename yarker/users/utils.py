from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    mail_subject = "Активация аккаунта"
    message = render_to_string(
        "activation_email.html",
        {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )
    send_mail(
        mail_subject,
        message,
        "superpolimer123@yandex.ru",
        [
            user.email,
        ],
    )
