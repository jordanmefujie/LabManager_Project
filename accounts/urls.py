from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordResetConfirmView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
