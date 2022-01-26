from django.views import generic

from todo_list.models import ToDoTask, ToDoList
from todo_list.forms import ToDoTaskForm

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

class ToDoTaskNestedMixin:
    def get_object(self, queryset=None):
        todo_list = get_object_or_404(ToDoList, pk=self.kwargs['list_pk'])

        return get_object_or_404(ToDoTask, pk=self.kwargs['task_pk'], todo_list=todo_list)
    
    def get_success_url(self):
        return f"/{self.kwargs['list_pk']}/"

class ToDoTaskCreateView(generic.CreateView):
    model = ToDoTask
    form_class = ToDoTaskForm
    template_name = "todo_task/create.html"

    def form_valid(self, form):
        todo_list = get_object_or_404(ToDoList, pk=self.kwargs['list_pk'])
        self.object = form.save(commit=False)
        self.object.todo_list = todo_list
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return f"/{self.kwargs['list_pk']}/"

class ToDoTaskUpdateView(ToDoTaskNestedMixin, generic.UpdateView):
    model = ToDoTask
    form_class = ToDoTaskForm
    template_name = 'todo_task/update.html'

class ToDoTaskDeleteView(ToDoTaskNestedMixin, generic.DeleteView):
    model = ToDoTask


def task_done_action(request, list_pk, task_pk):
    todo_list = ToDoList.objects.get(pk=list_pk)
    task = ToDoTask.objects.get(pk=task_pk, todo_list=todo_list)

    task.done = True
    task.save()

    return redirect(reverse('todo_list:detail', args=(list_pk)))