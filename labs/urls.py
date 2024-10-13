# labs/urls.py
from django.urls import path
from .views import large_lab_form_view
from . import views

urlpatterns = [
    path('search-labs/', views.search_labs, name='search_labs'),
    path('large-form/', large_lab_form_view, name='large_lab_form'),
    path('request-test/', views.large_form_view, name='large_form'),
]
