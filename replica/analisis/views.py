from django.shortcuts import render
from .forms import AnalisisForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .logic.logic_analisis import get_analisis
import json

def analisis_list(request):
    measurements = get_analisis()
    context = list(measurements.values())
    return JsonResponse(context, safe=False)