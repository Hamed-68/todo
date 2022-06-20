from django import forms
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# --------------- PROFILE FORM ------------------------------------
class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ('photo',)

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