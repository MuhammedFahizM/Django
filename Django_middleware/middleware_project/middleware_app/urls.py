# from django.urls import path
# from django.contrib import admin

# from middleware_app import views

# urlpatterns = [
   

#     path('abcd/', views.home),
#     path('admin/', admin.site.urls),
#     path('home/', views.home),
#     path('about/', views.about),


# ]

from django.contrib import admin
from django.urls import path
from middleware_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('teacher_home/', views.teacher_home, name='teacher_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('principal_home/', views.principal_home, name='principal_home'),   
     
]