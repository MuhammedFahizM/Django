from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerialzer
# Create your views here.

# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerialzer



# Customized : added filter options.


# class TaskViewSet(ModelViewSet):
#     serializer_class = TaskSerialzer

#     def get_queryset(self):
#         return Task.objects.filter(completed = True) # only returns incomplet tasks.


from rest_framework.response import Response
from rest_framework.decorators import action


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzer

    @action(detail=False,methods=['get'])
    def completed(self,request):
        completed_tasks = Task.objects.filter(completed = True)
        serializer = self.get_serializer(completed_tasks,many = True)
        return Response(serializer.data) 

