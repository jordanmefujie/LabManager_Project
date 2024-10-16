from django.urls import path
from .views import contact_view, services_view, about_view, login_view, register_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('services/', services_view, name='services'),
    path('about/', about_view, name='about'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
