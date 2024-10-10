from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stores, name='view_stores'),  # Home view for stores
    path('stores', views.logistics_overview, name='logistics_overview'),
    path('stores/', views.view_stores, name='view_stores'),
    path('stores/<int:pk>/', views.logistic_detail, name='logistic_detail'),
    path('calendar/', views.stock_calendar, name='stock_calendar'),
    path('add-commodity/', views.add_commodity, name='add_commodity'),
    path('commodity-list/', views.commodity_list, name='commodity_list'),
    path('delete-commodity/<int:pk>/', views.delete_commodity, name='delete_commodity'),
    path('filter-logistics/', views.filter_logistics, name='filter_logistics'),
    path('update-logistics/<int:pk>/', views.update_logistics, name='update_logistics'),
#    path('update-logistics/', views.update_logistics, name='update_logistics'),
#    path('stores/dashboard/', views.dashboard_view, name='dashboard'),
]
