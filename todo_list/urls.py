from django.urls import path
from todo_list import views

app_name = "todo_list"

urlpatterns = [
    # Lists
    path("", views.ToDoListIndexView.as_view(), name='index'),
    path("<int:pk>/", views.ToDoListDetailView.as_view(), name='detail'),
    path("create/", views.ToDoListCreateView.as_view(), name='create'),
    path("<int:pk>/delete/", views.ToDoListDeleteView.as_view(), name='delete'),
    path("<int:pk>/update/", views.ToDoListUpdateView.as_view(), name='update'),

    # Tasks
    path("<int:list_pk>/tasks/create/", views.ToDoTaskCreateView.as_view(), name='task_create'),
    path("<int:list_pk>/tasks/<int:task_pk>/", views.ToDoTaskUpdateView.as_view(), name='task_update'),
    path("<int:list_pk>/tasks/<int:task_pk>/delete/", views.ToDoTaskDeleteView.as_view(), name='task_delete'),
]