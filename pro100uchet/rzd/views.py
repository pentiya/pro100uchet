from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django_tables2 import SingleTableView

#from rzd.models import Doroga
from rzd.models import Region
from .models import Station
#from rzd.models import Zdanie

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations':stations})
#    return render(request, 'station_list.html', {'station': Station.objects.all()})

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region_list.html', {'regions':regions})


from .tables import StationTable

class StationListView(SingleTableView):
    model = Station
    table = StationTable
    template_name = 'station_table.html'


#def doroga_list(request):
#    dorogas = Doroga.objects.all()
#    return render(request, 'doroga_list.html', {'dorogas':dorogas})

#class DorogaListView(ListView):
#    model = Doroga
#    template_name = 'doroga.html'
#    queryset = Service.objects.all().order_by('kod')
#
#class RegionListView(ListView):
#    model = Region
#    template_name = 'Region.html'
#    queryset = Service.objects.all().order_by('name')
