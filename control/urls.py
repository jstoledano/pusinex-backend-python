from django.urls import path, re_path
from rest_framework import routers
from control.views import (
    MunicipioViewSet, LocalidadViewSet, SeccionViewSet,  PusinexViewSet,
    Index,
)

router = routers.SimpleRouter()

router.register(r'municipio', MunicipioViewSet)
router.register(r'seccion', SeccionViewSet)
router.register(r'localidad', LocalidadViewSet)
router.register(r'pusinex', PusinexViewSet)

urlpatterns = [
    path('', Index.as_view(), name='index')
]
