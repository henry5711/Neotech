"""
URL configuration for neotech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.CustomLogout, name='logout'),
    path('edit_profile/', views.EditProfile, name='edit_profile'),
    path('perfil/', views.Perfil, name='perfil'),
    path('cambiar_clave/', views.Cambiar_clave, name='cambiar_clave'),
    path('curso/', views.ver_cursos, name='cursos'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('lecciones/<int:leccion_id>/', views.detalle_leccion, name='detalle_leccion'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)