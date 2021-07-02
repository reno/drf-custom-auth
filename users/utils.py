from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.tokens import email_confirmation_token


def send_confirmation_email(user, domain):
    subject = 'Django app account verification'
    context = {
        'user': user,
        'domain': domain,
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_confirmation_token.make_token(user),
    }
    message = render_to_string('confirmation_email.html', context)
    user.email_user(subject, message)