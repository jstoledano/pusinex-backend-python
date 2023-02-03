import django_filters
from django.db.models import Q
from django.forms.widgets import Input
from control.models import Localidad


class LocalidadFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='filtro_localidad',
        label=None,
        widget = Input(attrs={
            'placeholder':'buscar por localidad o municipio',
            'class': 'form-control form-control-lg py-3',
            'type': 'text',
            'aria-label': '.form-control-lg example'
        })
    )
    class Meta:
        model = Localidad
        fields = ['q', ]

    def __init__(self, *args, **kwargs):
        super(LocalidadFilter, self).__init__(*args, **kwargs)
        # self.form.initial['id_q'] = 'Hola'
        self.filters['q'].label = ''
        if self.data == {}:
            self.queryset = self.queryset.none()

    def filtro_localidad(self, queryset, name, value):
        valor = 0
        try:
            valor = int(value)
        except ValueError:
            return queryset.filter(
                Q(nombre__icontains=value) |
                Q(municipio__nombre__icontains=value)
            )
        return queryset.filter(municipio__seccion__seccion=valor)
        