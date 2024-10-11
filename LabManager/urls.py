"""
URL configuration for LabManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from blog import views
from demo import views
from dashboard import views
from home import views
from settings import views
from accounts import views
from labmanagement import views
from reports import views
from Links import views
from stores import views
from notifications import views
from labs import views

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('blog/', include('blog.urls')),
#    path('', views.home, name='home'),
#    path('about/', views.about, name='about'),
#    path('contact/', views.contact, name='contact'),
#    path('services/', views.services, name='services')
# ]


urlpatterns = [
# base url for blog

path('blog/', include('blog.urls')),
# base url for demo
path('demo/', include('demo.urls')),

# for dasboard, home and accounts.
path('', include('home.urls')),  # Home page and related URLs
path('dashboard/', include('dashboard.urls')),
path('accounts/', include('django.contrib.auth.urls')),
path('labmanagement/', include('labmanagement.urls')),  # Add this line
path('reports/', include('reports.urls')),  # Add this line
path('settings/', include('settings.urls')),  # Add this line
path('Links/', include('Links.urls')),
path('accounts/', include('accounts.urls')),
# base url fo stores
path('stores/', include('stores.urls')),
path('notifications/', include('notifications.urls')),
path('labs/', include('labs.urls')),
]
