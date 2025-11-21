from django.shortcuts import render,HttpResponse

from celery_app.task import add

# Create your views here.


def test(request):
    add.delay(5,6)
    return HttpResponse("success")