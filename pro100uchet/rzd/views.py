from django.shortcuts import render

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from rzd.models import Doroga
from rzd.models import Doroga
from rzd.models import Otdelenie
from rzd.models import Stanciya
from rzd.models import Zdanie

def doroga_list(request):
    dorogas = Doroga.objects.all()
    return render(request, 'doroga_list.html', {'dorogas':dorogas})

"""

def otdelenie_list(request):
    otdelenies = otdelenie.objects.all()
    return render(request, 'otdelenie_list.html', {'otdelenies':otdelenies})

def stanciya_list(request):
    stations = Stanciya.objects.all()
    return render(request, 'station_list.html', {'stations':stations})
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
#class OtdelenieListView(ListView):
#    model = Otdelenie
#    template_name = 'otdelenie.html'
#    queryset = Service.objects.all().order_by('name')
