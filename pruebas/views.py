from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tracking.models import Tracking
from recon.static.py import arduino
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def pruebas_index(request):
    if request.method == 'POST':
        return render(request, 'pruebasIndex.html', { 'status': 'Order Found' })
    else:
        return render(request, 'pruebasIndex.html', { 'status': 'Invalid Access' })

# Scripts to send/receive data from Arduino and Raspberry Pi
@csrf_exempt
def leerArduino(request):
    if request.method == 'POST':
        data = arduino.receiveData()
        # if data contains the keys 'error' or 'warning', return the data as is
        if 'error' in data or 'warning' in data:
            return JsonResponse(data)
        for key in data:
            if data[key] == 'True':
                data[key] = True
            elif data[key] == 'False':
                data[key] = False
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Invalid Access"})
    
@csrf_exempt
def enviarArduino(request):
    if request.method == 'POST':
        data = arduino.sendData(request.POST['dato'])
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Invalid Access"})
    
