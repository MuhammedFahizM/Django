from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView,TaskDeleteView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/view/', TaskDetailView.as_view(), name='task_detail'), 
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),  
]