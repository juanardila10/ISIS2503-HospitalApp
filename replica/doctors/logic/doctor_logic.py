from ..models import Doctor

def create_doctor(form):
    doctor=Doctor()
    doctor.name = form["name"]
    doctor.save()
    return doctor