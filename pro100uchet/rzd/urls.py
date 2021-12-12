from django.urls import path
from . import views

from rzd.views import RegionListView
from rzd.views import StationListView

from rzd.views import RegionTableView
from rzd.views import StationTableView

from rzd.views import RegionCreateView

urlpatterns = [
    path('', views.rzd_index, name='rzd_index'),
#    path('', views.region_list, name='region_list'),
    path('doroga_list/', views.doroga_list, name='doroga_list'),
    path('region_list/', views.region_list, name='region_list'),
    path('station_list/', views.station_list, name='station_list'),

    path('region_listview/', RegionListView.as_view(), name='region_listview'),
    path('station_listview/', StationListView.as_view(), name='station_listview'),

    path('region_add/', RegionCreateView.as_view(), name='region_add' ),

    path('region_tableview/', RegionTableView.as_view(), name='region_tableview'),
    path('station_tableview/', StationTableView.as_view(), name='station_tableview'),
]
