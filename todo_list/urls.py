from django.urls import path
from todo_list import views

app_name = "todo_list"

urlpatterns = [ 
    path("", views.ToDoListIndexView.as_view(), name='index'),
    path("<int:pk>/", views.ToDoListDetailView.as_view(), name='detail'),
    path("create/", views.ToDoListCreateView.as_view(), name='create'),
]