from django.urls import path
from rest_framework import routers
from views import (
    MunicipioViewSet,
    LocalidadViewSet,
    SeccionViewSet,
    PusinexViewSet
)

router = routers.SimpleRouter()

router.register(r'municipio', MunicipioViewSet)
router.register(r'seccion', SeccionViewSet)
router.register(r'localidad', LocalidadViewSet)
router.register(r'pusinex', PusinexViewSet)

urlpatterns = router.urls
