from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
#DetailView для отображения динамической страницы
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


def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'main/index.html')

def rzd_map(request):
    stations = Station.objects.all()
    return render(request, 'rzd-map.html', {'stations': stations})

#отображение на основе функции
def doroga_list(request):
    dorogas = Doroga.objects.all()
    return render(request, 'rzd/doroga_list.html', {'dorogas':dorogas})

##отображение на основе предопределенного класса
#class DorogaListView(ListView):
#    model = Doroga
#    template_name = 'rzd/doroga_list.html'
#    context_object_name = 'dorogas' # default doroga_list
##    queryset = Service.objects.all().order_by('kod')

def doroga_add(request):
    error = ''
    if request.method == 'POST':        # нажата кнопка Добавить
        form = DorogaForm(request.POST) # получаем данные с формы ввода
        if form.is_valid(): #проверяем корректность данных
            form.save()
            return redirect('doroga') #need import redirect
        else:
            error = 'Форма неверна'

    form = DorogaForm()
    data = {
      'form': form,
      'error': error,
    }
    return render(request, 'rzd/doroga_create.html', data)

class DorogaDetailView(DetailView):
    model = Doroga
    template_name = 'rzd/doroga_detail.html'
    context_object_name = 'doroga' #название ключа, по которому запись передантся внутрь шаблона

class DorogaUpdateView(UpdateView):
    model = Doroga
    template_name = 'rzd/doroga_create.html'
    #fields = ['name', 'short_name', 'kod'] #use form_class
    form_class = DorogaForm

class DorogaDeleteView(DeleteView):
    model = Doroga
    success_url = '/rzd/doroga/'
    template_name = 'rzd/doroga_delete.html'

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'rzd/region_list.html', {'regions':regions})

def region_add(request):
    form = RegionForm()
    data = {
      'form': form,
    }
    return render(request, 'rzd/region_add.html', data)

def station_list(request):
    stations = Station.objects.all()
    data = []
    data.append( {'name':'11', 'kod':'12'} )
    data.append( {'name':'21', 'kod':'22'} )
    for ss in stations:
      data.append( {'name': ss, 'kod':'22'} )

    #data.append(['name' : '2'])
    #[]
    #"1","2","3"
    #}
    return render(request, 'station_list.html', {'data':data})
#    return render(request, 'station_list.html', {'station': Station.objects.all()})

class StationListView(ListView):
    model = Station
    template_name = 'station_list.html' #default rzd/station_list.html
    context_object_name = 'stations' # default station_list

class StationDetailView(DetailView):
    model = Station
    template_name = 'station_detail.html' #default rzd/station_detail.html

class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html' #default rzd/region_list.html
    context_object_name = 'regions' # default region_list

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
