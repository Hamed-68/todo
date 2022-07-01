from django.urls import path
from task import views


app_name = 'task'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete'),
]