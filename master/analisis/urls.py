from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('analisiscreate/', csrf_exempt(views.analisis_create), name='analisisCreate'),
]