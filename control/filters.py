import django_filters
from control.models import Localidad


class LocalidadFilter(django_filters.FilterSet):
    class Meta:
        model = Localidad
        fields = {
            'nombre': ['icontains', ],
            'municipio__nombre': ['icontains', ]
        }