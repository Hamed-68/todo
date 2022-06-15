from calendar import Calendar
from logging import PlaceHolder
from django import forms
from task.models import Task
from django.contrib.admin.widgets import AdminDateWidget


class TaskForm(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ('title', 'notes', 'priority', 'due_date')
        widgets = {
            'due_date': AdminDateWidget(attrs={'placeholder': 'YYYY-MM-DD'})
        }


class SearchForm(forms.Form):                           # for filter tasks by date
    date = forms.DateField(widget=AdminDateWidget())