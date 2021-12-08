from django.contrib import admin

# Register your models here.
from .models import Ivc
from .models import Rivc
from .models import Usel
#from .models import UselType

admin.site.register(Ivc)
#@admin.register(Ivc) 
#class RegionAdmin(admin.ModelAdmin):
#    list_display = ('name',)

admin.site.register(Rivc)
#@admin.register(Region) 
#class RegionAdmin(admin.ModelAdmin):
#    list_display = ('name', 'ivc')

admin.site.register(Usel)
#@admin.register(Usel)
#class UselAdmin(admin.ModelAdmin):
#   list_display = ('name', 'station','region', 'ivc')

#admin.site.register(UselType)
