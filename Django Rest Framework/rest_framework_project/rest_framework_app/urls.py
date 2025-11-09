from django.urls import path

from rest_framework_app import views
urlpatterns = [
    
    path('get_books/',views.get_books,name='get_books'),

]