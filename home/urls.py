from django.urls import path
from .views import home_view, contact_view, services_view, about_view, register, apps_link_view, views_login

urlpatterns = [
        path('', home_view, name='home'),
        path('contact/', contact_view, name='contact'),
        path('services/', services_view, name='services'),
        path('about/', about_view, name='about'),
        path('register/', register, name='register'),
	path('login/', views_login, name='login'),
	path('apps_link/', apps_link_view, name='apps_link')
	]
