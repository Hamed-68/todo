from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ('title', 'notes', 'priority', 'due_date')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class SearchByDateForm(forms.Form):                           # for filter tasks by date
    date = forms.DateField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
)

class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'search title or note'})
    )

class SearchPriorityForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = ('priority',)
        widgets = {'priority': forms.Select()}