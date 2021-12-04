from django.urls import path
from . import views

from rzd.views import StationListView

urlpatterns = [
#    path('', views.doroga_list, name='doroga_list'),
    path('station/', StationListView.as_view()),
    path('station_list/', views.station_list, name='station_list'),
#    path('doroga/', views.doroga_list, name='doroga_list'),
]

"""
urlpatterns = [
 #   path('', views.station_list, name='station_list'),
    path('rzd/', views.doroga_list, name='doroga_list'),
    path('doroga/', views.doroga_list, name='doroga_list'),
    path('station/', views.station_list, name='station_list'),
#    path('station/', views.Station_list, name='station_list'),
]

"""