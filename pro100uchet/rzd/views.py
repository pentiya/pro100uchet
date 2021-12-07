from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from .models import Station

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations':stations})


class StationListView(ListView):
    model = Station
#    template_name = 'rzd/templates/station.html'
    template_name = 'station.html'
#    queryset = Service.objects.all().order_by('kod')



#from rzd.models import Doroga
#from rzd.models import Region
#from rzd.models import Station
#from rzd.models import Zdanie



#def doroga_list(request):
#    dorogas = Doroga.objects.all()
#    return render(request, 'doroga_list.html', {'dorogas':dorogas})

"""

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'Region_list.html', {'regions':regions})

"""
"""
def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations':stations})

def doroga_list(request):
    dorogas = Doroga.objects.all()
    return render(request, 'doroga_list.html', {'dorogas':dorogas})

"""


#class DorogaListView(ListView):
#    model = Doroga
#    template_name = 'doroga.html'
#    queryset = Service.objects.all().order_by('kod')
#
#class RegionListView(ListView):
#    model = Region
#    template_name = 'Region.html'
#    queryset = Service.objects.all().order_by('name')
