from django.contrib import admin
from .models import Municipio, Seccion, Localidad, Pusinex


class PusinexInline(admin.TabularInline):
    model = Pusinex
    extra = 1


class SeccionAdmin(admin.ModelAdmin):
    ordering = ['distrito', 'municipio', 'seccion']
    list_filter = ['distrito', 'municipio']
    inlines = [PusinexInline]


class LocalidadAdmin(admin.ModelAdmin):
    ordering = ['municipio', 'localidad']
    list_filter = ['municipio']
    inlines = [PusinexInline]


admin.site.register(Municipio)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Pusinex)
