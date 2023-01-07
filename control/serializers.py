from rest_framework import serializers
from control.models import (
    Municipio,
    Seccion,
    Localidad,
    Pusinex)


class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = '__all__'
        depth = 3


class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        fields = '__all__'
        depth = 2


class LocalidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Localidad
        fields = '__all__'
        depth = 2


class PusinexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pusinex
        fields = '__all__'
        depth = 3
