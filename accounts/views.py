from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


# -------------------- USER REGISTER ---------------------------------------
class UserCreateView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('task:home')
    form_class = UserRegisterForm

# -------------------- UPDATE USER ---------------------------------------
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('task:home')
    form_class = UserUpdateForm