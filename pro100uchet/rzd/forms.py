from django.forms import ModelForm, TextInput, NumberInput

#ModelForm для наследования
#TextInput для описания поля ввода текста

from .models import Doroga
from .models import Region

class DorogaForm(ModelForm):
    class Meta:
        model = Doroga
        fields = ['name', 'short_name', 'kod']
        widgets = {
          "name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Название дороги', }),
          "short_name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Краткое название дороги', }),
          "kod":  NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Код дороги', }),
        }


class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'kod', 'doroga']
        widgets = {
          "name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Название региона', }),
          "kod":  NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
#          "doroga":  FieldInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
        }
