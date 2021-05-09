from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__' #all fields should be shown
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Tasks')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Tasks'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) #to ensure that a user only has access to their own data
        context['Tasks'] = context['Tasks'].filter(user=self.request.user)
        context['count'] = context['Tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('Tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('Tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('Tasks')
