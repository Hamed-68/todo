from django import forms
from task.models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Div
from crispy_forms import layout, bootstrap


# ===================================== TASK FORM ===================================
class TaskForm(forms.ModelForm):
    
    class Meta():
        model = Task
        fields = ('title', 'notes', 'priority', 'passed', 'due_date')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'},),
            'notes': forms.Textarea(attrs={'style': 'height: 4em'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('title', css_class='col-6'),
                    Div('due_date', css_class='col-6'),
                    css_class = 'row'
                ),
                Div(
                    Div('notes', css_class='col')
                ),
                Div(
                    Div('passed', css_class='col-6'),
                    Div('priority', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Add', css_class='btn btn-primary'),
                    css_class='d-flex justify-content-center mt-2')
                ),
            )
        )

# ===================================== SEARCH BY DATE FORM =========================
class SearchByDateForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div('date', css_class='d-flex me-2'),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Search', css_class='btn btn-primary'),
                    css_class='col-2-sm')
                ),
                css_class="d-flex justify-content-center"
            )
        )

# ===================================== SEARCH FORM =================================
class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'search title or note'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div('search', css_class='d-flex me-2'),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Search', css_class='btn btn-primary'),
                    css_class='col-2-sm')
                ),
                css_class="d-flex justify-content-center"
            )
        )

# ===================================== SEARCH PRIORITY FORM ========================
class SearchPriorityForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = ('priority',)
        widgets = {'priority': forms.Select()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div('priority', css_class='d-flex me-2'),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Select', css_class='btn btn-primary'),
                    css_class='col-2-sm')
                ),
                css_class="d-flex justify-content-center"
            )
        )