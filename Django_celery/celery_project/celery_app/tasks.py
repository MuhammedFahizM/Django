from celery import shared_task

# @shared_task
# def add(x,y):
#     return x + y

from django.core.mail import send_mail
from celery import shared_task
from celery_project import settings

@shared_task(bind=True)
def send_email_task(self):
    mail_subject = "Hi from celery"
    message = "I have completed this task by celery"
    to_email = "muhammedjalal928@gmail.com"

    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
    return "Email sent Successfully"

