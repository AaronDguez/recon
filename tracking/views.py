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
        result: JsonResponse = addTracking.addTracking(request.POST)
        
        return tracking_index(request, status=result)
    else:
        return tracking_index(request, status=JsonResponse({'status': 'Invalid Access'}))

@csrf_exempt
def updateTrack(request):
    pass