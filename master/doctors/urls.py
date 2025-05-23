from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('doctorcreate/', csrf_exempt(views.doctor_create), name='doctorCreate'),
]