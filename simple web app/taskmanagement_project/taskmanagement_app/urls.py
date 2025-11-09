from taskmanagement_app import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('add_task/',views.add_task,name='add_task'),

]