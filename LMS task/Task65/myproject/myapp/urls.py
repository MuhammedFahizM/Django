# from django.urls import path
# from .views import about

# urlpatterns = [
#     path("about/", about, name="about"),
# ]

# from django.urls import path
# from .views import feedback_view

# urlpatterns = [
#     path("feedback/", feedback_view, name="feedback"),
# ]

# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # existing paths
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path
# from .views import profile_view

# urlpatterns = [
#     path("profile/<int:id>/", profile_view, name="profile"),
# ]

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import register_view, dashboard_view

# urlpatterns = [
#     path("register/", register_view, name="register"),
#     path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
#     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
#     path("dashboard/", dashboard_view, name="dashboard"),
# ]

# from django.urls import path
# from .views import home, add_task

# urlpatterns = [
#     path("", home, name="home"),
#     path("add/", add_task, name="add_task"),
# ]

# from django.urls import path
# from .views import TaskListView, TaskCreateView, TaskDeleteView

# urlpatterns = [
#     path("", TaskListView.as_view(), name="task_list"),
#     path("add/", TaskCreateView.as_view(), name="task_add"),
#     path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    

# ]

from django.urls import path
from .views import (
    favorite_movie,
    clear_movie_session,
    theme_view,
    clear_theme_cookie,
)

urlpatterns = [
    path("movie/", favorite_movie, name="favorite_movie"),
    path("movie/clear/", clear_movie_session, name="clear_movie"),
    path("theme/", theme_view, name="theme"),
    path("theme/clear/", clear_theme_cookie, name="clear_theme"),
]
