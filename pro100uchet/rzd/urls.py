from django.urls import path
from . import views

urlpatterns = [
    path('', views.doroga_list, name='doroga_list'),
    path('doroga/', views.doroga_list, name='doroga_list'),
]

"""
urlpatterns = [
 #   path('', views.station_list, name='station_list'),
    path('rzd/', views.doroga_list, name='doroga_list'),
    path('doroga/', views.doroga_list, name='doroga_list'),
    path('station/', views.station_list, name='station_list'),
#    path('station/', views.stanciya_list, name='station_list'),
]

"""