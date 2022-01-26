from django import forms
from todo_list.models import ToDoList

class ToDoListForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    
    class Meta:
        model = ToDoList
        fields = ['name', 'description', 'due_date']