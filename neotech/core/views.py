from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UserProfileForm
from .models import Course, UserProfile, Lesson
from .forms import ChangePasswordForm


@login_required
def EditProfile(request):
    # Obtener o crear el UserProfile asociado al usuario
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request, 'Cambios guardados exitosamente.')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'Partials/UserEdit/Edit_profile.html', {'form': form})

@login_required(login_url='/login/')
def Cambiar_clave(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')  # Cambia 'index' al nombre de tu vista principal
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'Partials/UserEdit/Cambiar_clave.html', {'form': form})

def Register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('edit_profile')  # Redirigir a la página de perfil
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
    

# Supongo que tienes una vista llamada editar_perfil

@login_required(login_url='/login/')
def Index(request):
    cursos = Course.objects.all()
    return render(request, 'index.html', {'cursos': cursos})
    
def LoginView(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirigir a la página de inicio después del inicio de sesión
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def CustomLogout(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de inicio después del cierre de sesión

def Perfil(request):
    return render(request, 'Partials/UserEdit/Perfil.html')

def ver_cursos(request):
    # Obtener todos los cursos de la base de datos
    cursos = Course.objects.all()

    # Pasa los cursos a la plantilla
    return render(request, 'courses.html', {'cursos': cursos})

def cursos_hardware(request):
    cursos = Course.objects.filter(type_course__name='hardware')
    context = {'cursos': cursos, 'tipo_curso': 'hardware'}
    return render(request, 'hardware.html', context)

def cursos_programacion(request):
    cursos = Course.objects.filter(type_course__name='programacion')
    context = {'cursos': cursos, 'tipo_curso': 'programacion'}
    return render(request, 'programacion.html', context)

def cursos_software(request):
    cursos = Course.objects.filter(type_course__name='software')
    context = {'cursos': cursos, 'tipo_curso': 'software'}
    return render(request, '.html', context)

def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})