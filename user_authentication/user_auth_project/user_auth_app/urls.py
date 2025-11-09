from django.urls import path

from user_auth_app import views

urlpatterns = [

    path('accounts/sign_up/',views.sign_up,name="sign_up"),
    path('accounts/login/',views.loginview,name="login"),
    path('logout',views.logoutview,name="logout"),
    path('home',views.home,name="home"),
    path('resetPassword',views.resetPassword,name="resetPassword"),
    path('reset/',views.reset,name="reset")

]