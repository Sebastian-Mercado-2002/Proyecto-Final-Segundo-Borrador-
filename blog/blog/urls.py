"""
URL configuration for blog project.

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
from .views import index, aplicacion_de_la_ia, impacto_educacion, impacto_laboral, acerca_de, contacto, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('aplicacion_de_la_ia.html', aplicacion_de_la_ia, name='aplicacion_de_la_ia_html'),
    path('impacto_educacion.html', impacto_educacion, name='impacto_educacion'),
    path('impacto_laboral.html', impacto_laboral, name='impacto_laboral'),
    path('acerca_de.html', acerca_de, name='acerca_de'),
    path('contacto.html', contacto, name='contacto'),
    path('inicio.html', inicio, name='inicio')
]
