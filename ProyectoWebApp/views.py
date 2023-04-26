from django.shortcuts import render, HttpResponse

def  home(request):

    return render(request,"ProyectoWebApp/Home.html")

def  servicios(request):

    return render(request,"ProyectoWebApp/Servicios.html")

def  tienda(request):

    return render(request,"ProyectoWebApp/Tienda.html")

def  blog(request):

    return render(request,"ProyectoWebApp/Blog.html")

def  contacto(request):

    return render(request,"ProyectoWebApp/Contacto.html")
