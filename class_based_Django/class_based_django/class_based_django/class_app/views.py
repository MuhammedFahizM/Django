from django.shortcuts import render


from django.views.generic import ListView,DetailView,CreateView
from .models import Task
# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name='task/task_list.html'
    context_object_name='tasks'



from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class TaskCreateView(CreateView):
    model=Task
    fields=['name','completed']
    template_name='task/task_form.html'
    success_url=reverse_lazy('task_list')


from django.views.generic.edit import DeleteView

class TaskDetailView(DetailView):
    model=Task
    template_name='task/task_details.html'
    context_object_name='task'


class TaskDeleteView(DeleteView):
    model=Task
    template_name='task/task_confirm_delete.html'
    success_url=reverse_lazy('task_list')