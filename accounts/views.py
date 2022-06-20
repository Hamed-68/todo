from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from accounts.models import Profile
from django.contrib.auth.models import User
from accounts.forms import ProfileForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


# -------------------- USER REGISTER ---------------------------------------
class UserCreateView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('task:home')
    form_class = UserRegisterForm

    def form_valid(self, form):
        self.object = form.save()
        Profile.objects.create(user=self.object)
        return super(UserCreateView, self).form_valid(form)

# -------------------- UPDATE USER ---------------------------------------
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('task:home')
    form_class = UserUpdateForm
    profile_form = ProfileForm
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.request.user)
        context['profile_form'] = self.profile_form(instance=self.request.user.profile)
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST, instance=request.user)
            profile_form = self.profile_form(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile_form.save(commit=False)
                profile_form.user = user
                profile_form.save()
                return redirect(self.success_url)
        return super(UserUpdateView, self).post(request, *args, **kwargs)