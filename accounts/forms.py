from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# --------------- USER REGISTER FORM -------------------------------
class UserRegisterForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

# --------------- USER UPDATE FORM ---------------------------------
class UserUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')