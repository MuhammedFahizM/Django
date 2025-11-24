# from django.shortcuts import render,HttpResponse

# from celery_app.task import add

# Create your views here.


# def test(request):
#     add.delay(5,6)
#     return HttpResponse("success")


from django.http import HttpResponse
from django.shortcuts import render
from celery_app.tasks import send_email_task


def send_email_to_all(request):
    send_email_task.delay()
    return HttpResponse("Sent Email Successfully....Check your mail please")