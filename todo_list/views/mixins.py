from todo_list.models import ToDoTask, ToDoList

from django.shortcuts import get_object_or_404

class ToDoTaskNestedMixin:
    def get_object(self, queryset=None):
        todo_list = get_object_or_404(ToDoList, pk=self.kwargs['list_pk'])

        return get_object_or_404(ToDoTask, pk=self.kwargs['task_pk'], todo_list=todo_list)
    
    def get_success_url(self):
        return f"/{self.kwargs['list_pk']}/"
