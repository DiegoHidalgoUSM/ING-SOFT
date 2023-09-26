from django.contrib.auth import authenticate, login as auth_login  # Cambia el nombre de la función 'login'
from django.shortcuts import render, redirect
from core.models import Comunicado, Categoria
from django.contrib import messages

def index(request):
    nivelPOST = request.POST.get('nivel', None)
    categoriaPOST= request.POST.get('categoria', None)
    comunicados = Comunicado.objects.order_by('-fecha_envio')
    categorias = Categoria.objects.all()

    if nivelPOST:
        comunicados = comunicados.filter(nivel=nivelPOST)
    
    if categoriaPOST:
        comunicados = comunicados.filter(categoria_id=categoriaPOST)
    
    data = {
        'comunicados': comunicados,
        'categorias': categorias
    }

    return render(request, 'core/index.html', data)


def iniciar_sesion(request):  # Cambia el nombre de la vista
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Iniciar sesión si las credenciales son correctas
            auth_login(request, user)  # Utiliza el nuevo nombre 'auth_login'
            return redirect('/admin/')
        else:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            messages.error(request, 'Credenciales incorrectas. Intente nuevamente.')

    return render(request, 'core/login.html')