from django.urls import path
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
#    path('', views.region_list, name='region_list'),
    path('map/', views.rzd_map, name='rzd-map'),

#    path('doroga/', views.doroga_list, name='doroga'),
    path('doroga/', views.DorogaListView.as_view(), name='doroga'),
    path('doroga/add/', views.doroga_add, name='doroga_add'),
    path('doroga/<int:pk>', views.DorogaDetailView.as_view(), name='doroga_view'),
    path('doroga/<int:pk>/update', views.DorogaUpdateView.as_view(), name='doroga_update'),
    path('doroga/<int:pk>/delete', views.DorogaDeleteView.as_view(), name='doroga_delete'),

#    path('region/', views.region_list, name='region'),
    path('region/', views.RegionListView.as_view(), name='region'),
    path('region/add/', views.region_add, name='region-add' ),
    path('region/<int:pk>', views.RegionDetailView.as_view(), name='region-view'),
    path('region/<int:pk>/update', views.RegionUpdateView.as_view(), name='region-update'),
    path('region/<int:pk>/delete', views.RegionDeleteView.as_view(), name='region-delete'),
#    path('region_tableview/', RegionTableView.as_view(), name='region_tableview'),
#    path('region_add/', RegionCreateView.as_view(), name='region_add' ),
#    path('region_check/', views.region_add, name='region_check' ),

    path('station/', views.StationListView.as_view(), name='station'),
    path('station/add/', views.station_add, name='station-add' ),
    path('station/<int:pk>/', views.StationDetailView.as_view(), name='station-view'),
    path('station/table/', views.StationTableView.as_view(), name='station-table'),
    path('station/<int:pk>/update', views.StationUpdateView.as_view(), name='station-update'),
    path('station/<int:pk>/delete', views.StationDeleteView.as_view(), name='station-delete'),
]
