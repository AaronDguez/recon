from django.shortcuts import render
from tracking.models import Tracking
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def searchTracking(request):
    if request.method == 'POST':
        track = request.POST.get('track', '').strip()
        if not track:
            return render(request, 'busqueda.html', { 'status': 'No Tracking Number Provided' })
        trackedOrder: Tracking = Tracking.objects.filter(trackNumber=track).first()
        if(trackedOrder):
            return render(request, 'busqueda.html', { 'status': 'Order Found', 'track': trackedOrder })
        else:
            return render(request, 'busqueda.html', { 'status': 'Order Not Found' })
    else:
        return render(request, 'busqueda.html', { 'status': 'Invalid Access' })
