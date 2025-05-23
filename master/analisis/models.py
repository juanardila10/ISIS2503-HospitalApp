from django.db import models
from dj_cqrs.mixins import MasterMixin
from doctor.models import Doctor

class Analisis(MasterMixin, models.Model):

    CQRS_ID = 'analisis_model'

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    paciente = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    examen = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)