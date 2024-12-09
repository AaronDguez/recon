from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchTracking(request, track: str):
    if(track == ''):
        return render(request, 'searchTracking.html', { 'status': 'No Tracking Number Provided' })
    if(request.method == 'GET'):
        pass
    else:
        return render(request, 'searchTracking.html', { 'status': 'Invalid Access' })