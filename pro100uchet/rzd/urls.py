from django.urls import path
from . import views

from rzd.views import RegionListView
from rzd.views import StationListView

from rzd.views import RegionTableView
from rzd.views import StationTableView

from rzd.views import RegionCreateView

urlpatterns = [
#    path('', views.index, name='index'),
#    path('', views.region_list, name='region_list'),
    path('map/', views.rzd_map, name='rzd-map'),

    path('doroga/', views.doroga_list, name='doroga'),
    path('doroga/add/', views.doroga_add, name='doroga_add'),
    path('doroga/<int:pk>', views.DorogaDetailView.as_view(), name='doroga_view'),
    path('doroga/<int:pk>/update', views.DorogaUpdateView.as_view(), name='doroga_update'),
    path('doroga/<int:pk>/delete', views.DorogaDeleteView.as_view(), name='doroga_delete'),

    path('region/', views.region_list, name='region'),
#    path('region_listview/', RegionListView.as_view(), name='region_listview'),
#    path('region_tableview/', RegionTableView.as_view(), name='region_tableview'),
    path('region_add/', views.region_add, name='region_add' ),
#    path('region_add/', RegionCreateView.as_view(), name='region_add' ),
#    path('region_check/', views.region_add, name='region_check' ),

    path('station/', views.station_list, name='station'),
#    path('station_listview/', StationListView.as_view(), name='station_listview'),
    path('station_tableview/', StationTableView.as_view(), name='station_tableview'),
]
