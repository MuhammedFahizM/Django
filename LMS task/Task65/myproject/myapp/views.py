# Create your views here.


# from django.shortcuts import render

# def about(request):
#     return render(request, "about.html")

from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, "feedback_success.html", form.cleaned_data)
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})

from django.shortcuts import render, get_object_or_404
from .models import Profile

def profile_view(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, "profile.html", {"profile": profile})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")


from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect("home")
    return render(request, "add_task.html")

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView):
    model = Task
    fields = ["title"]
    template_name = "add_task.html"
    success_url = reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")

from django.shortcuts import render, redirect

def favorite_movie(request):
    if request.method == "POST":
        request.session["favorite_movie"] = request.POST.get("movie")
        return redirect("favorite_movie")

    movie = request.session.get("favorite_movie")
    return render(request, "favorite_movie.html", {"movie": movie})


def clear_movie_session(request):
    request.session.pop("favorite_movie", None)
    return redirect("favorite_movie")


from django.http import HttpResponse
from django.shortcuts import render

def theme_view(request):
    theme = request.COOKIES.get("theme")

    if request.method == "POST":
        theme = request.POST.get("theme")
        response = render(request, "theme.html", {"theme": theme})
        response.set_cookie("theme", theme)
        return response

    return render(request, "theme.html", {"theme": theme})


def clear_theme_cookie(request):
    response = render(request, "theme.html")
    response.delete_cookie("theme")
    return response
