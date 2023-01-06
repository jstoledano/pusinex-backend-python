from django.views.generic import ListView
from control.models import Municipio, Seccion, Localidad, Pusinex


class MunicipioListView(ListView):
    model = Municipio
