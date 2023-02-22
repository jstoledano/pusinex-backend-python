# coding: utf-8
"""Formularios para Gestión de PUSINEX."""

#         app: control
#      módulo: forms
# descripción: Formularios para PUSINEX
#       autor: Javier Sanchez Toledano
#       fecha: 25 de enero de 2023

from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML, Field, Button
from crispy_forms.bootstrap import InlineRadios, Tab, TabHolder, FormActions
from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from django.shortcuts import render, redirect
from control.models import Pusinex, Municipio, Localidad, Seccion, Revision


class PUSINEXForm(forms.Form):
    seccion = forms.IntegerField()
    localidad = forms.IntegerField()
    f_act = forms.DateField()
    hojas = forms.IntegerField()
    archivo = forms.FileField()
    observaciones = forms.CharField(widget=forms.Textarea, required=False)

    def crear_o_buscar_pusinex(self, seccion, localidad):
        """Crea o busca un PUSINEX en la base de datos."""
        try:
            pusinex = Pusinex.objects.get(seccion=seccion, localidad=localidad)
        except Pusinex.DoesNotExist:
            seccion_obj = Seccion.objects.get(pk=seccion)
            localidad_obj = Localidad.objects.get(pk=localidad)
            pusinex = Pusinex.objects.create(seccion=seccion_obj, localidad=localidad_obj, activo=True)
        return pusinex

    def crear_revision(self, pusinex):
        """Crea una revisión de PUSINEX."""
        if self.request.method == 'POST':
            form = PUSINEXForm(self.request.POST)
            if form.is_valid():
                revision = Revision.objects.create(pusinex=pusinex, **form.cleaned_data)
                return redirect('control:pusinex_detail', pk=revision.pk)
        else:
            form = PUSINEXForm()
        return render(self.request, 'control/pusinex_form.html', {'form': form})