from django.urls import path
from task import views


app_name = 'task'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='task'),
    path('detail/<int:pk>/', views.DetailTask.as_view(), name='task_detail'),
]