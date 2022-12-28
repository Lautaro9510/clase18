from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


from familia.models import Familia

# Create your views here.

def crear_familiar(request):
    nuevo_familiar = Familia.objects.create(nombre= 'Nahuel',anio_nacimiento= 1990, casado= False)
    print(nuevo_familiar)
    return HttpResponse('Un miembro de la familia se ha añadido')

def lista_familia(request):
    familia_entera = Familia.objects.all()
    print(familia_entera)
    context = {
        'Familia':familia_entera,
    }
    return render(request, 'lista_familia.html', context=context)