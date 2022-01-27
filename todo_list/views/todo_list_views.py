from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from todo_list.models import ToDoList
from todo_list.forms import ToDoListForm

class ToDoListIndexView(generic.ListView):
    model = ToDoList
    template_name = "todo_list/index.html"
    context_object_name = "todos"

class ToDoListCreateView(generic.CreateView):
    model = ToDoList
    form_class = ToDoListForm
    template_name = 'todo_list/create.html'
    success_url = reverse_lazy('todo_list:index')

class ToDoListUpdateView(generic.UpdateView):
    model = ToDoList
    form_class = ToDoListForm
    template_name = "todo_list/update.html"
    success_url = reverse_lazy('todo_list:index')

class ToDoListDeleteView(generic.DeleteView):
    model = ToDoList
    success_url = reverse_lazy('todo_list:index')

class ToDoListDetailView(generic.DetailView):
    model = ToDoList
    template_name = "todo_list/detail.html"
    context_object_name = "todo"
