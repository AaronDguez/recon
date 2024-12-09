from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tracking.models import Tracking
import threading

# Create your views here.
@csrf_exempt
def pruebas_index(request):
    if request.method == 'POST':
        track = request.POST.get('track', '').strip()
        trackedOrder: Tracking = Tracking.objects.filter(trackNumber=track).first()
        if(trackedOrder):
            return render(request, 'pruebasIndex.html', { 'status': 'Order Found', 'track': trackedOrder.to_dict() })
        else:
            return render(request, 'pruebasIndex.html', { 'status': 'Order Not Found' })
    else:
        return render(request, 'pruebasIndex.html', { 'status': 'Invalid Access' })

# Scripts to send/receive data from Arduino and Raspberry Pi