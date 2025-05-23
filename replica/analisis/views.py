from django.shortcuts import render
from .forms import AnalisisForm
from django.contrib import messages
from django.http import HttpResponse
from .logic.logic_analisis import create_analisis
import json

def analisis_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        analisis = create_analisis(data_json)
        if(analisis):
            return HttpResponse('Successfully created measurement')
        else:
           return HttpResponse('Error creating measurement, variable does not exist')
    else:
        form = AnalisisForm()

    context = {
        'form': form,
    }

    return render(request, 'Analisis/analisisCreate.html', context)