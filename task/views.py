from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from task.models import Task
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from task.forms import TaskForm


# ------------------------ TASK LIST -----------------------------------
class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task/home.html'

    def get_queryset(self):
        user = self.request.user
        today = timezone.now().date()
        # list today's tasks belong request.user
        queryset = Task.objects.filter(user=user, due_date__date=today)
        return queryset

# ------------------------ TASK DETAIL -----------------------------------
class DetailTask(LoginRequiredMixin, DetailView):
    template_name = 'task/detail.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset

# ------------------------ CREATE TASK -----------------------------------
class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

# ------------------------ UPDATE TASK -----------------------------------
class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'task/update.html'
    form_class = TaskForm
    success_url = reverse_lazy('task:home')
    model = Task

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset