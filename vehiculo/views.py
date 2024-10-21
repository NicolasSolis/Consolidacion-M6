from django.shortcuts import render, redirect
from .models import VehiculoModel
from .forms import VehiculoForm

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
    else:
        form = VehiculoForm()

    return render(request, 'add_vehiculo.html', {'form': form})

def view_vehiculo(request): #comprobar si funciona
    vehiculos = VehiculoModel.objects.all()
    return render(request, 'view_vehiculo.html', {'vehiculos':vehiculos})