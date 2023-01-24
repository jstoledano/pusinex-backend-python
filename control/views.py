from django.views.generic import TemplateView
from rest_framework import viewsets

from control import filters
from control.serializers import MunicipioSerializer, SeccionSerializer, LocalidadSerializer, PusinexSerializer
from control.models import Municipio, Seccion, Localidad, Pusinex
from control.filters import LocalidadFilter
from django_filters.rest_framework import DjangoFilterBackend


class Index(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs) # get the default context data
        context['filter'] = LocalidadFilter(self.request.GET, queryset=Localidad.objects.all())
        return context


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer


class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.LocalidadFilter


class PusinexViewSet(viewsets.ModelViewSet):
    queryset = Pusinex.objects.all()
    serializer_class = PusinexSerializer
    filterset_fields = ['localidad__nombre', ]
