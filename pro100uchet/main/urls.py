from django.urls import path, include
from . import views

#from .views import web_index

#app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('rzd/', include('rzd.urls')),
]
