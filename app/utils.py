# myapp/utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(user):
    subject = 'Welcome to our site!'
    body = render_to_string('mail.html', {'user': user})
    send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=body)

