from django.contrib import admin

# Register your models here.

"""
#Register export-import module
from import_export import resources
from import_export.admin import ImportExportModelAdmin
"""

# Register your models here.
from .models import Doroga
#admin.site.register(Doroga)

"""
class DorogaResource(resources.ModelResource):
    class Meta:
        model = Doroga
#        skip_unchanged = True
#        report_skipped = False
#        import_id_fields = ('kod',)
        fields = ('id', 'name', 'kod', 'short_name',)

class DorogaAdmin(ImportExportModelAdmin):
    resource_class = DorogaResource
admin.site.register(DorogaAdmin)
"""

admin.site.register(Doroga)


from .models import Region
#admin.site.register(Region)

"""
class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
#        skip_unchanged = True
#        report_skipped = False
#        import_id_fields = ('kod',)
        fields = ('id', 'name', 'kod', 'doroga',)

class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource
admin.site.register(RegionAdmin)
"""

admin.site.register(Region)

from .models import Station
#admin.site.register(Station)

"""
class StationResource(resources.ModelResource):
    class Meta:
        model = Station
#        skip_unchanged = True
#        report_skipped = False
#        import_id_fields = ('kod',)
        fields = ('id', 'name', 'kod', 'Region',)

class StationAdmin(ImportExportModelAdmin):
    resource_class = StationResource

admin.site.register(StationAdmin)
"""

admin.site.register(Station)

from .models import Zdanie
admin.site.register(Zdanie)

"""
# Register your models here.
from .models import Doroga
from .models import Region
from .models import Station

#admin.site.register(Doroga)
@admin.register(Doroga)
class DorogaAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod')
 #   list_filter = ('region')
 #   ordering = ('name')

#admin.site.register(Region)
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod', 'doroga')
 #   list_filter = ('region')
 #   ordering = ('name')

#admin.site.register(Station)
@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod', 'Region')
 #   list_filter = ('region')
 #   ordering = ('name')
"""
