from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .forms import VehiculoForm
from .models import Vehiculo

# INICIO DE SESIÓN
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return redirect('index') 
            else:
                messages.error(request, "Nombre de usuario o contraseña no válidos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña no válidos.")
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})

# CIERRE DE SESIÓN
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return redirect('index')  

#INDEX
def index(request):
    return render(request, 'vehiculo/index.html')

#AGREGAR VEHICULO

@login_required
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': VehiculoForm(), 
                'alert_message': 'El vehículo ha sido agregado correctamente.',
                'alert_type': 'success'
            }
        else:
            context = {
                'form': form,
                'alert_message': 'No se pudo agregar el vehículo. Por favor, verifica los datos ingresados.',
                'alert_type': 'danger'
            }
        return render(request, 'vehiculo/agregar_vehiculo.html', context)
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

#LISTAR VEHICULOS
@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all() 
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})