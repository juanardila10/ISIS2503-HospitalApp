from django.db import models
from dj_cqrs.mixins import MasterMixin

class Doctor(MasterMixin, models.Model):

    CQRS_ID = 'doctor_model'

    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

