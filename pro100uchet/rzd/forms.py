from django.forms import ModelForm

from .models import Doroga
from .models import Region

class DorogaForm(ModelForm):
    class Meta:
        model = Doroga
        fields = ('name', 'kod', 'short_name')

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ('name', 'kod', 'doroga')
