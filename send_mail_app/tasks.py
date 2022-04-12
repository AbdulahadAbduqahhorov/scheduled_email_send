from celery import shared_task
from django.core.mail import send_mail
from send_mail import settings
from send_mail_app.models import SendEmail


@shared_task
def send_mail_func(subject, message):
    sendmail = SendEmail.objects.get(subject=subject, message=message)
    users = sendmail.to_email.all()
    for user in users:
        mail_subject = subject
        message = message
        to_email = user.user_email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
