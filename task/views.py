from django.shortcuts import render
from django.views.generic import ListView, DetailView
from task.models import Task
from django.utils import timezone


# ------------------------ TASK LIST -----------------------------------
class TaskListView(ListView):
    template_name = 'task/home.html'

    def get_queryset(self):
        user = self.request.user
        today = timezone.now().date()
        # list today's tasks belong request.user
        queryset = Task.objects.filter(user=user, due_date__date=today)
        return queryset

# ------------------------ TASK LIST -----------------------------------
class DetailTask(DetailView):
    template_name = 'task/detail.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset
