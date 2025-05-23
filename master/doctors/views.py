from django.shortcuts import render
from django.http import HttpResponse
from .forms import DoctorForm
from .logic.doctor_logic import create_doctor
import json

def doctor_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        create_doctor(data_json)
        return HttpResponse('Successfully created variable')
    else:
        form = DoctorForm()

    context = {
        'form': form,
    }
    return render(request, 'Doctor/doctorCreate.html', context)