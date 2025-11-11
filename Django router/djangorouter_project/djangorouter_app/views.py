from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from.models import Task
from .serializers import TaskSerialzer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class TaskViewSet(ModelViewSet):
    queryset  = Task.objects.all()
    serializer_class = TaskSerialzer

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzer