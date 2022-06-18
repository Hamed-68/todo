from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm



class UserCreateView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('task:home')
    form_class = UserRegisterForm

    def form_valid(self, form):
        self.object = form.save()
        Profile.objects.create(user=self.object)
        return super(UserCreateView, self).form_valid(form)









# def register(request):
#     template_name = 'accounts/signup.html'
#     success_url = reverse('task:home')

#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             Profile.objects.create(user=user)
#             return success_url
#     else:
#         form = UserRegisterForm()
#     return render(request, template_name, {'form': form})