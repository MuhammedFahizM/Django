from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .pagination import CustomPagination


from .models import Task
from .serializers import TaskSerialzer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzer
    pagination_class = CustomPagination

    #both searching and filtering

    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['task_name']



          # Filtering
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['completed']

     # Searching 
    # filter_backends = [SearchFilter]
    # search_fields = ['task_name']  # search by 'task_name' field