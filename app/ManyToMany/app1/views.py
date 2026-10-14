from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from app1.models import *


def listaVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request,'lista_vehiculo.html', {'vehiculo':vehiculos})

def detalleVehiculo(request, idVehiculo):
    vehiculo = get_object_or_404(
        Vehiculo.objects.prefetch_related(
            Prefetch(queryset=Actua.objects.select_related('Estacionamieto'))
        ),
        pk=idVehiculo
    )
    return render(request, 'detalle_vehiculo.html', {'vehiculo':vehiculo})


def listaEstacionemientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request,'lista_estacionamineto.html', {'estacionamiento':estacionamientos})

def detalleEstacioamiento(request, idEstacionamiento):
    estacionamiento = get_object_or_404(
        Estacionamiento.objects.prefetch_related(
            Prefetch(queryset=Actua.objects.select_related('Vehiculo'))
        ),
        pk=idEstacionamiento
    )
    return render(request, 'detalle_estacionamiento.html', {'estacionamiento':estacionamiento})



