from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aplicacion_de_la_ia(request):
    return render(request, 'aplicacion_de_la_ia.html')

def impacto_educacion(request):
    return render(request, 'impacto_educacion.html')

def impacto_laboral(request):
    return render(request, 'impacto_laboral.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')

def contacto(request):
    return render(request, 'contacto.html')

def inicio(request):
    return render(request, 'inicio.html') 