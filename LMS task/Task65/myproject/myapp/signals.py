from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def task_created(sender, instance, created, **kwargs):
    if created:
        print(f"New task created: {instance.title}")


@receiver(post_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    print(f"Task deleted: {instance.title}")


from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Welcome",
            message="Welcome to our platform.",
            from_email="admin@example.com",
            recipient_list=[instance.email],
            fail_silently=True,
        )
