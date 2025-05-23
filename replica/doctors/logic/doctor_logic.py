from ..models import Doctor

def get_doctors():
    queryset = Doctor.objects.all()
    return queryset


def create_doctor(form):
    doctor=Doctor()
    doctor.name = form["name"]
    doctor.save()
    return doctor