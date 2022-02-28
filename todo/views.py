from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks' # default value is 'object_list' 

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task' # default value is 'object' 
    template_name = 'todo/show.html'

class TaskCreate(CreateView):
    model = Task
    # fields = ['title', 'description']
    fields = '__all__'
    success_url = reverse_lazy('todo.index')

class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo.index')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo.index')

