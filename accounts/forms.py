from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms import layout, bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div


# --------------- USER REGISTER FORM -------------------------------
class UserRegisterForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            Div(
                Div(
                    Div('username', css_class='col-6'),
                    Div('email', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('first_name', css_class='col-6'),
                    Div('last_name', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('password1', css_class='col-6'),
                    Div('password2', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Sign up', css_class='btn btn-primary'),
                    css_class='d-flex justify-content-center mb-3')
                ),
            )
        )


# --------------- USER UPDATE FORM ---------------------------------
class UserUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            Div(
                Div(
                    Div('username', css_class='col-6'),
                    Div('email', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    Div('first_name', css_class='col-6'),
                    Div('last_name', css_class='col-6'),
                    css_class='row'
                ),
                Div(
                    bootstrap.FormActions(
                    layout.Submit('submit', 'Update', css_class='btn btn-primary'),
                    css_class='d-flex justify-content-center mt-2 mb-3')
                ),
            )
        )