from rest_framework import serializers
from . import models


class AnalisisSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'doctor', 'paciente', 'estado', 'examen')
        model = models.Analisis