from django.contrib import admin
from .models import Vehiculo

admin.site.site_header = 'Vehiculos' 
admin.site.index_title = 'Panel de control Proyecto Django'  
admin.site.site_title = 'Administrador Django'  

class MiappAdmin(admin.ModelAdmin):
    #Campo dinámico personalizado
    list_display = ('marca', 'modelo', 'precio', 'clasificacion_precio')
    
    def clasificacion_precio(self, obj):
        if obj.precio >= 0 and obj.precio <= 10000:
            return "Bajo"
        elif obj.precio > 10000 and obj.precio <= 30000:
            return "Medio"
        else:
            return "Alto"


admin.site.register(Vehiculo, MiappAdmin)