from django.urls import path
from . import views

from rzd.views import StationListView
from rzd.views import StationTableView
from rzd.views import RegionCreateView

urlpatterns = [
    path('', views.station_list, name='station_list'),
#    path('', views.region_list, name='region_list'),
    path('doroga_list/', views.doroga_list, name='doroga_list'),
    path('region_list/', views.region_list, name='region_list'),
    path('station_list/', views.station_list, name='station_list'),

    path('station/', StationListView.as_view(), name='station'),

    path('region_add/', RegionCreateView.as_view(), name='region_add' ),

    path('station_table/', StationTableView.as_view()),
]
