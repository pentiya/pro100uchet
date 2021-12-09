from django.urls import path
from . import views

from rzd.views import StationListView

urlpatterns = [
    path('', views.station_list, name='station_list'),
#    path('', views.region_list, name='region_list'),
#    path('doroga/', views.doroga_list, name='doroga_list'),
    path('region_list/', views.region_list, name='region_list'),
    path('station_list/', views.station_list, name='station_list'),
    path('station/', StationListView.as_view()),
]
