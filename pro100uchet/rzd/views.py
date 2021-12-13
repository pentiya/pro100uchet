from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.

from django_tables2 import SingleTableView

from .models import Doroga
from .models import Region
from .models import Station
#from rzd.models import Zdanie

from .forms import DorogaForm
from .forms import RegionForm

from .tables import RegionTable
from .tables import StationTable


def rzd_index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'rzd_index.html')

def doroga_list(request):
    dorogas = Doroga.objects.all()
    return render(request, 'doroga_list.html', {'dorogas':dorogas})

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region_list.html', {'regions':regions})

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations':stations})
#    return render(request, 'station_list.html', {'station': Station.objects.all()})

class DorogaListView(ListView):
    model = Doroga
    template_name = 'doroga_list.html'
    context_object_name = 'dorogas' # default station_list
#    queryset = Service.objects.all().order_by('kod')

class StationListView(ListView):
    model = Station
    template_name = 'station_list.html' #default rzd/station_list.html
    context_object_name = 'stations' # default station_list


class StationDetailView(DetailView):
    model = Station
    template_name = 'station_detail.html' #default rzd/station_detail.html


class RegionListView(ListView):
    model = Region

class RegionDetailView(DetailView):
    model = Region


class StationTableView(SingleTableView):
    model = Station
    table = StationTable
    template_name = 'station_table.html'

class RegionTableView(SingleTableView):
    model = Region
    table = RegionTable
    template_name = 'region_table.html'
#    queryset = Region.objects.all().order_by('kod')

class RegionCreateView(CreateView):
    template_name = 'region_create.html'
    form_class = RegionForm
    success_url = 'region_list/'



'''
class DorogaCreateView(CreateView):
    template_name = 'doroga_create.html'
    form_class = Doroga
    success_url = '/station/'
    def get_context_data(self, **kwargs):
	context = super().get_context_data(**kwargs)
	context[’dorogas’] = Doroga.objects.all()
	return context
'''