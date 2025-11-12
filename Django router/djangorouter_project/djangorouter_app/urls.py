from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,TaskList,TaskDetail

# router =  DefaultRouter()
# router.register(r'tasks',TaskViewSet,basename='task')

# urlpatterns = [
#     path('api/',include(router.urls)),

# ]

urlpatterns = [
    path('tasks/',TaskList.as_view(),name='task_list'),
    path('tasks/<int:pk>/',TaskDetail.as_view(),name='task_detail')
]
