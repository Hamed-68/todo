from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(success_url = reverse_lazy('accounts:password_change_done')),
        name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
        name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
]