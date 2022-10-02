from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Familiar
import datetime
# Create your views here.




def datos_de_familiares(request):
    plantilla = loader.get_template('template1.html')
    date_time_str_abuela = '1929-12-29'
    date_time_obj_abuela = datetime.datetime.strptime(date_time_str_abuela, '%Y-%m-%d')
    abuela = Familiar(nombre="Onelia", edad=92,fecha_de_nacimiento=date_time_obj_abuela)
    abuela.save()

    date_time_str_hermano_1 = '1997-8-27'
    date_time_obj_hermano_1 = datetime.datetime.strptime(date_time_str_hermano_1, '%Y-%m-%d')
    hermano_1 = Familiar(nombre="Emiliano", edad=25,fecha_de_nacimiento=date_time_obj_hermano_1)
    hermano_1.save()

    date_time_str_hermano_2 = '1995-10-26'
    date_time_obj_hermano_2 = datetime.datetime.strptime(date_time_str_hermano_2, '%Y-%m-%d')
    hermano_2 = Familiar(nombre="Angel", edad=27,fecha_de_nacimiento=date_time_obj_hermano_2)
    hermano_2.save()

    diccionario =  {    
        "abuela":abuela,
        "hermano_1":hermano_1,
        "hermano_2":hermano_2
    }

    documento = plantilla.render(diccionario)
    return HttpResponse(documento)