from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .logic.doctor_logic import get_doctors, create_doctor

def doctor_list(request):
    doctors = get_doctors()
    context = list(doctors.values())
    return JsonResponse(context, safe=False)