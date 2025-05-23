from doctors.models import Doctor
from ..models import Analisis

def get_analisis():
    queryset = Analisis.objects.all()
    return queryset


def create_analisis(form):
    doctor = None
    try:
        doctor = Doctor.objects.get(id=form["doctor"])
    except:
        return False
    if(doctor == None):
        return False
    else:
        analisis = Analisis()
        analisis.doctor = doctor
        analisis.paciente = form["paciente"]
        analisis.estado = "Procesando"
        analisis.examen = form["examen"]
        analisis.save()
        return True