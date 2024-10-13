# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='dashboard-home'),
        path('', views.dashboard_view, name='dashboard-home'),
        path('contact/', views.contact, name='dashboard-contact'),
        path('services/', views.services, name='dashboard-services'),
        path('about/', views.about, name='dashboard-about'),
        path('', views.dashboard_view, name='dashboard'),
	path('experiments/', views.experiments_view, name='experiments'),
	path('equipment/', views.equipment_view, name='equipment'),
	path('reports/', views.reports_view, name='dashboard-reports'),
	path('settings/', views.settings_view, name='dashboard-settings'),
        ]
