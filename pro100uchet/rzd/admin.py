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


from .models import Otdelenie
#admin.site.register(Otdelenie)

"""
class OtdelenieResource(resources.ModelResource):
    class Meta:
        model = Otdelenie
#        skip_unchanged = True
#        report_skipped = False
#        import_id_fields = ('kod',)
        fields = ('id', 'name', 'kod', 'doroga',)

class OtdelenieAdmin(ImportExportModelAdmin):
    resource_class = OtdelenieResource
admin.site.register(OtdelenieAdmin)
"""

admin.site.register(Otdelenie)

from .models import Stanciya
#admin.site.register(Stanciya)

"""
class StanciyaResource(resources.ModelResource):
    class Meta:
        model = Stanciya
#        skip_unchanged = True
#        report_skipped = False
#        import_id_fields = ('kod',)
        fields = ('id', 'name', 'kod', 'otdelenie',)

class StanciyaAdmin(ImportExportModelAdmin):
    resource_class = StanciyaResource

admin.site.register(StanciyaAdmin)
"""

admin.site.register(Stanciya)

from .models import Zdanie
admin.site.register(Zdanie)

"""
# Register your models here.
from .models import Doroga
from .models import Otdelenie
from .models import Station

#admin.site.register(Doroga)
@admin.register(Doroga)
class DorogaAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod')
 #   list_filter = ('region')
 #   ordering = ('name')

#admin.site.register(Otdelenie)
@admin.register(Otdelenie)
class OtdelenieAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod', 'doroga')
 #   list_filter = ('region')
 #   ordering = ('name')

#admin.site.register(Station)
@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'kod', 'otdelenie')
 #   list_filter = ('region')
 #   ordering = ('name')
"""
