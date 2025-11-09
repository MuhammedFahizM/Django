from django.shortcuts import redirect, render
from taskmanagement_app.models import Task
from taskmanagement_app.forms import TaskForm
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request,'home_page.html',{'tasks' : tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form' : form})