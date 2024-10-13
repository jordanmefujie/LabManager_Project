from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_notifications, name='get_notifications'),
    path('read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('notifications/', views.notifications, name='notifications'),
]
