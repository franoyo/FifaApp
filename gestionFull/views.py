
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            # Verifica si el usuario ya existe
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Ya existe un usuario con este correo electrónico.')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                messages.success(request, '¡Registro exitoso! Puedes iniciar sesión ahora.')
        else:
            messages.error(request, 'Las contraseñas no coinciden. Intenta nuevamente.')

    return render(request, 'index.html')
def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Autentica al usuario
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            user.is_superuser = True
            user.save()

            return redirect('/admin/')  # Redirige al panel de administración

        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo nuevamente.')

    return render(request, 'index.html')
