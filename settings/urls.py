from django.urls import path
from . import views

urlpatterns = [
        path('user/', views.user_settings, name='user_settings'),
        path('config/', views.app_config, name='app_config'),
        path('', views.settings_view, name='settings'),
	path('settings/', views.settings_view, name='dashboard-settings'),
        ]
