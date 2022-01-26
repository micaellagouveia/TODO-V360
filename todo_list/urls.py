from django.urls import path
from todo_list import views

app_name = "todo_list"

urlpatterns = [ 
    path("", views.ToDoListIndexView.as_view(), name='index'),
]