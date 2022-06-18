from django import forms
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ('photo',)


class UserRegisterForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email')