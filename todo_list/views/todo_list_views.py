from django.shortcuts import render
from django.views import generic

from todo_list.models import ToDoList

class ToDoListIndexView(generic.ListView):
    model = ToDoList
    template_name = "todo_list/index.html"
    context_object_name = "todos"
