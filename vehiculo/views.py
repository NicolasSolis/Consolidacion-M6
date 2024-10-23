from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel
from .forms import VehiculoForm, RegistroUsuarioForm

def view_registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            puede_ver = Permission.objects.get(codename='can_visualizar_catalogo', content_type=content_type)
            puede_añadir = Permission.objects.get(codename='add_vehiculomodel', content_type=content_type)
            user = form.save()
            user.user_permissions.add(puede_ver, puede_añadir)
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()

    return render(request=request, template_name="registro.html", context={"register_form": form})

#intenté hacerlo con clases, honestamente estoy cansado y no con mucho tiempo, así que será en funciones, perdón
#faltaba poner 'app.permission', me demoré un montón, antes de leer 5 minutos de documentación
@login_required(login_url='/vehiculo/login/')
@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            form = VehiculoForm()
    else:
        form = VehiculoForm()

    return render(request, 'add_vehiculo.html', {'form': form})

@login_required(login_url='/vehiculo/login/')
@permission_required('vehiculo.can_visualizar_catalogo', raise_exception=True)
def view_vehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    return render(request, 'view_vehiculo.html', {'vehiculos':vehiculos})


def view_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalido username o password.")
        else:
            messages.error(request, "Invalido username o password.")
    else:
        form = AuthenticationForm()
    
    return render(request=request, template_name="login.html", context={"login_form": form}) # hubo un problema relacionado a esto en la clase M6S9 con pasar al contexto "user":user, ahora está parcialmente renderizado

def view_logout(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')