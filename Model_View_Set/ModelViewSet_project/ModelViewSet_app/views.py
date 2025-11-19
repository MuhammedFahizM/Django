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


# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerialzer

#     @action(detail=False,methods=['get'])
#     def completed(self,request):
#         completed_tasks = Task.objects.filter(completed = True)
#         serializer = self.get_serializer(completed_tasks,many = True)
#         return Response(serializer.data) 


from rest_framework import status

# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerialzer

#     def create(self, request, *args, **kwargs):
        
#         # make request data mutable
#         data = request.data.copy()

#         # convert task name to uppercase
#         if 'task_name' in data:
#             data['task_name'] = data['task_name'].upper()

#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception = True)
#         self.perform_create(serializer)

#         return Response(serializer.data,status=status.HTTP_201_CREATED)

   


        # Handling Errors:-
        
from rest_framework.exceptions import ValidationError


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerialzer

    def create(self, request, *args, **kwargs):
        if not request.data.get('task_name'):
            raise ValidationError("Task name is required.")
        return super().create(request,*args,**kwargs)

