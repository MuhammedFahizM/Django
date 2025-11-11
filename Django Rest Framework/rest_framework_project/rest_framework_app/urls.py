from django.urls import path

from rest_framework_app import views
from rest_framework_app.views import TaskList,TaskListCreateAPIView

urlpatterns = [
    
    # path('get_books/',views.get_books,name='get_books'),
    # path('task_list/',views.task_list,name='task_list'),
    path('tasklist/',TaskList.as_view(),name="tasklist"),  # class based API
    path('generic_view/',TaskListCreateAPIView.as_view(),name='generic_view')   # generic view
]