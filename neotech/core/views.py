from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UserProfileForm
from .models import Course, UserProfile, Lesson,ProgressUser
from .forms import ChangePasswordForm
from django.db import transaction

@login_required
def EditProfile(request):
    # Obtener o crear el UserProfile asociado al usuario
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            # Verificar si el checkbox delete_profile_picture está seleccionado
            if form.cleaned_data.get('delete_profile_picture'):
                # Eliminar la foto de perfil
                user_profile.profile_picture.delete()

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request, 'Cambios guardados exitosamente.')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UserEdit/Edit_profile.html', {'form': form})
@login_required(login_url='/login/')
def Cambiar_clave(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')  # Cambia 'index' al nombre de tu vista principal
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'UserEdit/Cambiar_clave.html', {'form': form})

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
    return render(request, 'UserEdit/Perfil.html')

def ver_cursos(request):
    # Obtener todos los cursos de la base de datos
    cursos = Course.objects.all()

    # Pasa los cursos a la plantilla
    return render(request, 'cursos.html', {'cursos': cursos})

def ver_cursos_hardware(request):
    cursos_hardware = Course.objects.filter(type_course__name='hardware')
    return render(request, 'courses/cursos_hardware.html', {'cursos': cursos_hardware})

def ver_cursos_software(request):
    cursos_software = Course.objects.filter(type_course__name='software')
    return render(request, 'courses/cursos_software.html', {'cursos': cursos_software})

def ver_cursos_programacion(request):
    cursos_programacion = Course.objects.filter(type_course__name='programacion')
    return render(request, 'courses/cursos_programacion.html', {'cursos': cursos_programacion})

def lista_cursos(request):
    cursos = Course.objects.all()
    return render(request, 'courses/lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    usuario = request.user
    curso = get_object_or_404(Course, id=curso_id)
    lecciones = curso.lesson_set.all()
    progress=ProgressUser.objects.filter(course_id=curso_id,user_id=usuario.id).count()
    
    return render(request, 'courses/detalle_curso.html', {'curso': curso, 'lecciones': lecciones,'progress':progress})

def detalle_leccion(request, leccion_id):
    usuario = request.user
    leccion = get_object_or_404(Lesson, id=leccion_id)
    verifycateProgress=ProgressUser.objects.filter(lesson_id=leccion_id,user_id=usuario.id).count()
    x=0
    if verifycateProgress > 0:
        x=1
    return render(request, 'courses/detalle_leccion.html', {'leccion': leccion,'verify': x})

def progressLession(request):
    try:
        progress=ProgressUser.objects.create(
        user_id=request.GET.get('user_id'),
        lesson_id=request.GET.get('lesson_id'), 
        course_id=request.GET.get('course_id'),
        progress=True,
        ) 
        progress.save();
        return redirect('lista_cursos')
    except Exception as e:
        cursos = Course.objects.all()
        return render(request, 'index.html', {'cursos': cursos})