from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    due_date = models.DateField()

    def __str__(self):
        return self.name