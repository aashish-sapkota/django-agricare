from django.contrib import admin
from . models import Crop,Query
# Register your models here.


admin.site.register(Query)
class CropsAdmin(admin.ModelAdmin):
    list_display = ('Crop','start_date', 'est_harvest')

    def Crop(self,obj):
        return obj.name

    def start_date(self,obj):
         return obj.start_date


admin.site.register(Crop, CropsAdmin)