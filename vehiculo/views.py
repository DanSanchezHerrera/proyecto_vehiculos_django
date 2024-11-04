from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
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
    can_add_vehicle = request.user.is_authenticated and request.user.is_staff and request.user.has_perm('vehiculo.add_vehiculo')
    return render(request, 'vehiculo/index.html', {'can_add_vehicle': can_add_vehicle})

#AGREGAR VEHICULO

@permission_required('vehiculo.add_vehiculo', raise_exception=True)
@login_required
def agregar_vehiculo(request):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permiso para agregar vehículos.')
        return redirect('listar') 

    can_add_vehicle = request.user.is_authenticated and request.user.is_staff and request.user.has_perm('vehiculo.add_vehiculo')

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El vehículo ha sido agregado correctamente.')
            form = VehiculoForm()
        else:
            messages.error(request, 'No se pudo agregar el vehículo. Por favor, verifica los datos ingresados.')
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form, 'can_add_vehicle': can_add_vehicle})

#LISTAR VEHICULOS
@login_required
def listar_vehiculos(request):
    can_add_vehicle = request.user.is_authenticated and request.user.is_staff and request.user.has_perm('vehiculo.add_vehiculo')
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos, 'can_add_vehicle': can_add_vehicle})