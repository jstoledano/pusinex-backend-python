from django.contrib import admin
from .models import Entidad, Distrito, Municipio, Seccion, Localidad, Pusinex, Revision


class RevisionInLine(admin.TabularInline):
    model = Revision
    extra = 1


class PusinexAdmin(admin.ModelAdmin):
    ordering = ['seccion', 'localidad']
    list_filter = ['seccion__distrito', 'seccion__municipio']
    inlines = [RevisionInLine]


class PusinexInline(admin.TabularInline):
    model = Pusinex
    extra = 1


class SeccionAdmin(admin.ModelAdmin):
    ordering = ['distrito', 'municipio', 'seccion']
    list_filter = ['distrito', 'municipio']
    inlines = [PusinexInline]


class LocalidadAdmin(admin.ModelAdmin):
    ordering = ['municipio__municipio', 'localidad']
    inlines = [PusinexInline]


admin.site.register(Entidad)
admin.site.register(Distrito)
admin.site.register(Municipio)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Pusinex, PusinexAdmin)
