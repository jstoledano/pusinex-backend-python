from dal import autocomplete
from django.db.models import Q
from django.views.generic import FormView, TemplateView, DetailView, CreateView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from control import filters
from control.filters import LocalidadFilter
from control.forms import PUSINEXForm
from control.models import Localidad, Municipio, Pusinex, Seccion, Revision
from control.serializers import (LocalidadSerializer, MunicipioSerializer,
                                 PusinexSerializer, SeccionSerializer)

import logging

logger = logging.getLogger(__name__)


class Index(FilterView):
    template_name = 'index.html'
    model = Localidad
    filterset_class = LocalidadFilter

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['filter'] = LocalidadFilter(
            self.request.GET,
            queryset=Localidad.objects.order_by('municipio', 'localidad').select_related('municipio'),
        )
        return context


class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Municipio.objects.all()
        if self.q > "":
            qs = qs.filter(Q(nombre__istartswith=self.q))
        return qs


class PusinexDetail(DetailView):
    model = Pusinex
    context_object_name = 'pusinex'


class LocalidadDetail(DetailView):
    model = Localidad
    context_object_name = 'localidad'


class CreatePUSINEX(LoginRequiredMixin, CreateView):
    template_name = 'control/pusinex_form.html'
    form_class = PUSINEXForm
    model = Revision

    def form_invalid(self, form):
        logger.error(form.errors)
        return super(CreatePUSINEX, self).form_invalid(form)

    def form_valid(self, form):
        # Crea o busca un PUSINEX en la base de datos
        seccion = Seccion.objects.get(seccion=form.cleaned_data['seccion'])
        municipio = Municipio.objects.get(pk=seccion.municipio.id)
        localidad = Localidad.objects.get(localidad=form.cleaned_data['localidad'], municipio=municipio)
        try:
            pusinex = Pusinex.objects.get(seccion=seccion, localidad=localidad)
        except Pusinex.DoesNotExist:
            pusinex = Pusinex.objects.create(seccion=seccion, localidad=localidad, activo=True)
        # Crea una revisión de PUSINEX
        revision = form.save(commit=False)
        revision.pusinex = pusinex
        revision.save()
        return super(CreatePUSINEX, self).form_valid(form)

    def get_success_url(self):
        return reverse('localidad', kwargs={'pk': self.object.pusinex.localidad.id})


class Administration(TemplateView):
    template_name = 'administration.html'


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['municipio', 'seccion']


class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['municipio', ]


class PusinexViewSet(viewsets.ModelViewSet):
    queryset = Pusinex.objects.all()
    serializer_class = PusinexSerializer
    filterset_fields = ['id', 'seccion__seccion', 'localidad__localidad', ]
