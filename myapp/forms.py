from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(label='Task description', widget=forms.Textarea)