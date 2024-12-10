from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from recon import views
from pruebas.models import pruebas

# Create your views here.
@csrf_exempt
def pruebas_index(request):
    return render(request, 'pruebasIndex.html')

# Scripts to send/receive data from Arduino and Raspberry Pi
@csrf_exempt
def leerPruebas(request):
    if request.method == 'POST':
        # Read data from Arduino
        data = pruebas.objects.all().values()
        data = {
            'tamano': data[0]['tamano'],
            'color': data[0]['color'],
            'relleno': data[0]['relleno']
        }
        return JsonResponse(data, safe=False)
    else:
        return views.index(request)
