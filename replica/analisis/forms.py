from django import forms
from .models import Analisis

class AnalisisForm(forms.ModelForm):
    class Meta:
        model = Analisis
        
        fields=[
            'doctor',
            'paciente',
            'estado',
            'examen',
        ]

        labels = {
            'doctor' : 'Doctor',
            'paciente' : 'Paciente',
            'estado' : 'Estado',
            'examen' : 'Examen',
        }
