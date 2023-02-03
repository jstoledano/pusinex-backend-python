from django.urls import path, re_path
from rest_framework import routers
from control.views import (
    MunicipioViewSet, LocalidadViewSet, SeccionViewSet,  PusinexViewSet,
    Index, Administration, CreatePUSINEX,
    PusinexDetail, LocalidadDetail,
    MunicipioAutoComplete
)

router = routers.SimpleRouter()

router.register(r'municipio', MunicipioViewSet)
router.register(r'seccion', SeccionViewSet)
router.register(r'localidad', LocalidadViewSet)
router.register(r'pusinex', PusinexViewSet)

urlpatterns = [
    re_path(r'^municipio-autocomplete/$', MunicipioAutoComplete.as_view(), name='municipio-autocomplete'),
    path('pusinex/<int:pk>', PusinexDetail.as_view(), name='pusinex'),
    path('localidad/<int:pk>', LocalidadDetail.as_view(), name='localidad'),
    path('creation/', CreatePUSINEX.as_view(), name='create'),
    path('bgd/', Administration.as_view(), name='bgd'),
    path('', Index.as_view(), name='index')
]
