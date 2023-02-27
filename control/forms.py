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
        exclude = ('pusinex', )
        model = Revision
