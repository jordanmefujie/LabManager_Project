# labs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search-labs/', views.search_labs, name='search_labs'),
]
