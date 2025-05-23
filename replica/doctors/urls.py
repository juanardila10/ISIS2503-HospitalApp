from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('doctors/', views.doctor_list,name='doctor_list'), 
]