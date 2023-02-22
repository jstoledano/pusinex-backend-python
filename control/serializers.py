from rest_framework import serializers
from control.models import (
    Municipio,
    Seccion,
    Localidad,
    Pusinex,
    Revision
)


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


class RevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = '__all__'


class PusinexSerializer(serializers.ModelSerializer):
    rev = serializers.SerializerMethodField()

    class Meta:
        model = Pusinex
        fields = '__all__'
        depth = 3

    def get_rev(self, obj):
        revision = Revision.objects.filter(pusinex=obj).last()
        serializer = RevisionSerializer(revision, many=False)
        return serializer.data
