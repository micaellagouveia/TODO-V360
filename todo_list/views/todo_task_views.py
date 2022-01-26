from django.views import generic

from todo_list.models import ToDoTask, ToDoList
from todo_list.forms import ToDoTaskForm

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

class ToDoTaskCreateView(generic.CreateView):
    model = ToDoTask
    form_class = ToDoTaskForm
    template_name = "todo_task/create.html"

