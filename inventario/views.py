from django.shortcuts import render

# Create your views here.
def inventario_index(request):
    return render(request, 'mainInv.html')

def agregar_inventario(request):
    return render(request, 'viewAgregarInve.html')

def cantidad_inventario(request):
    return render(request, 'viewCantidad.html')

def ver_inventario(request):
    return render(request, 'viewInventario.html')