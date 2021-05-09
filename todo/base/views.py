from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__' #all fields should be shown
    success_url = reverse_lazy('Tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__' #all fields should be shown
    success_url = reverse_lazy('Tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('Tasks')
