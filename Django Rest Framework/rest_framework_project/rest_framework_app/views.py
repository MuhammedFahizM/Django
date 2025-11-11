# from django.shortcuts import render

# # Create your views here.

# from rest_framework.decorators import api_view
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework.response import Response

# # creating API VIEWS with DRF


# @api_view(['GET'])
# def get_books(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many = True)
#     return Response(serializer.data)



# from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(['GET','POST'])
# def task_list(request):
#     if request.method == 'GET':
#         tasks = [{'id':1,'name':'Learn DRF','completed': False}]
#         return Response(tasks)
#     elif request.method == 'POST':
#         new_task = request.data
#         return Response({'message':'Task created!','task':new_task})


from rest_framework.views import APIView


class TaskList(APIView):
    def get(self,request):
        tasks = [{'id':1,'name':'Learn DRF','completed':False}]
        return Response(tasks)
    
    def post(self,request):
        new_task = request.data
        return Response({'message':'Task created!','task':new_task})
    

            # using Generic views:-


from rest_framework.generics import ListCreateAPIView
from .models import Task
from .serializers import TaskSerialzer

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzer
    