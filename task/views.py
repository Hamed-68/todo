from django.shortcuts import render
from django.views.generic import ListView, DetailView
from task.models import Task
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin



# ------------------------ TASK LIST -----------------------------------
class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task/home.html'

    def get_queryset(self):
        user = self.request.user
        today = timezone.now().date()
        # list today's tasks belong request.user
        queryset = Task.objects.filter(user=user, due_date__date=today)
        return queryset

# ------------------------ TASK LIST -----------------------------------
class DetailTask(LoginRequiredMixin, DetailView):
    template_name = 'task/detail.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset
