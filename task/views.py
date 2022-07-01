from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from task.models import Task
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from task.forms import TaskForm, SearchByDateForm, SearchForm, SearchPriorityForm
from django.db.models import Q


# ------------------------ TASK LIST -----------------------------------
class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task/home.html'

    def get_queryset(self):               # list tasks by date or search belong user
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        if self.request.GET.get('date'):
            date = self.request.GET.get('date')
            try:
                queryset = queryset.filter(due_date__date=date)
            except ValidationError:
                return None
        elif self.request.GET.get('search'):
            search = self.request.GET.get('search')
            queryset = queryset.filter(Q(title__icontains=search) | Q(notes__icontains=search))
        elif self.request.GET.get('priority'):
            priority = self.request.GET.get('priority')
            queryset = queryset.filter(priority=priority)
        return queryset
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchByDateForm       # form for search tasks by date
        search_form = SearchForm      # from for search tasks by title or note
        priority_form = SearchPriorityForm      # filter by priority
        context['form'] = form
        context['search_form'] = search_form
        context['priority_form'] = priority_form
        return context

# ------------------------ CREATE TASK -----------------------------------
class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task:home')

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

# ------------------------ DELETE TASK -----------------------------------
class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = 'task/delete.html'
    success_url = reverse_lazy('task:home')

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset