# coding: utf-8
"""Formularios para Gestión de PUSINEX."""

#         app: control
#      módulo: forms
# descripción: Formularios para PUSINEX
#       autor: Javier Sanchez Toledano
#       fecha: 25 de enero de 2023


from django import forms
from control.models import Revision
import logging

logger = logging.getLogger(__name__)


class PUSINEXForm(forms.ModelForm):
    seccion = forms.IntegerField()
    localidad = forms.IntegerField()
    f_act = forms.DateField()
    hojas = forms.IntegerField()
    archivo = forms.FileField()
    observaciones = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        exclude = ('pusinex', 'user', )
        model = Revision
