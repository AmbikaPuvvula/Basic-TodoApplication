from TodoApp.models import Task
from django.forms import ModelForm
from django import forms


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = "__all__"
