from django.contrib import admin

from .models import ToDoList, ToDoTask

admin.site.register(ToDoList)
admin.site.register(ToDoTask)