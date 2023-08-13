from django.shortcuts import render, redirect

# forms.py
from .forms import RegistrarUsuarioForm

# importar AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
# importar logout, login, authenticate
from django.contrib.auth import authenticate, login, logout

# messages
from django.contrib import messages

# decoradores
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')
    
def registro(request):
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()

            messages.success(request, f'Nueva cuenta creada: {user.username}')
            return redirect('inicio')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = RegistrarUsuarioForm()

    return render(
        request=request,
        template_name='registro.html',
        context={"form":form}
    )

def custom_login(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate (
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user}')
                return redirect('inicio')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = AuthenticationForm()

    return render(
        request=request,
        template_name='login.html',
        context={'form':form}
    )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, f'Sesión finalizada')
    return redirect ('inicio')
