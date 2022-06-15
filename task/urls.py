from django.urls import path
from task import views


app_name = 'task'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailTask.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update'),
]