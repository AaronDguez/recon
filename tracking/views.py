from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import Tracking
from recon.static.py import addTracking, updateTrack

# Create your views here.
def tracking_index(request, page=1, status:JsonResponse=None):
    tracking_list = Tracking.objects.all().order_by('trackNumber')
    paginator = Paginator(tracking_list, 10)
    
    page_obj = paginator.get_page(page)
    pages = paginator.num_pages
    
    return render(request, 'mainTrack.html', {
        'page_obj': page_obj,
        'pages': range(1, pages + 1),
        'current_page': page,
        'status': status
    })

@csrf_exempt  
def addTrack(request):
    if request.method == 'POST':
        return addTracking.addTracking(request.POST)
    else:
        return JsonResponse({'status': 'Invalid Access'})

@csrf_exempt
def updTrack(request):
    if request.method == 'POST':
        return updateTrack.updateTrack(request.POST)
    else:
        return JsonResponse({'status': 'Invalid Access'})
    
@csrf_exempt
def getTracking(request):
    if request.method == 'POST':
        track = request.POST['track']
        order = Tracking.objects.get(trackNumber=track)
        if order.procesado == False and order.armado == False and order.prueba != False and order.etiquetado == None and order.enviado == None:
            return JsonResponse({"status": "Orden encontrada y lista para pruebas." })
        elif order.procesado == None or order.armado == None:
            return JsonResponse({"status": "Orden encontrada pero no ha sido procesada o armada." })
        elif order.prueba == False:
            return JsonResponse({"status": "Orden encontrada pero ya fue probada." })
        else:
            return JsonResponse({"status": "Orden encontrada pero ya fue etiquetada y/o enviada." })
    else:
        return JsonResponse({"error": "Invalid Access"})
    
@csrf_exempt
def saveTracking(request):
    if request.method == 'POST':
        track = request.POST['track']
        pasoPrueba = request.POST['pasoPrueba']
        order = Tracking.objects.get(trackNumber=track)
        order.prueba = False if pasoPrueba == 'true' else True
        order.save()
        return JsonResponse({"status": "Orden guardada correctamente." })
    else:
        return JsonResponse({"error": "Invalid Access"})