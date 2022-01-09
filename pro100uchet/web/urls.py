from django.urls import path
from . import views

#from .views import web_index

#app_name = 'web'

urlpatterns = [
    path('', views.web_index, name='web_index'),
]
