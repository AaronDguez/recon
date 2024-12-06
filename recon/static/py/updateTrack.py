from tracking.models import Tracking
from django.http import JsonResponse

"""
    This function updates an order in the database.
    trackData: dict - Dictionary with the order data from the form.
"""
def updateTrack(trackData:dict):
    trackNumber = trackData.get('trackNumber')
    clientName = trackData.get('clientName')
    procesado = trackData.get('procesado')
    if procesado == "":
        procesado = None
    elif procesado == "True":
        procesado = True
    else:
        procesado = False
    armado = trackData.get('armado')
    if armado == "":
        armado = None
    elif armado == "True":
        armado = True
    else:
        armado = False
    probado = trackData.get('prueba')
    if probado == "":
        probado = None
    elif probado == "True":
        probado = True
    else:
        probado = False
    etiquetado = trackData.get('etiquetado')
    if etiquetado == "":
        etiquetado = None
    elif etiquetado == "True":
        etiquetado = True
    else:
        etiquetado = False
    enviado = trackData.get('enviado')
    if enviado == "":
        enviado = None
    elif enviado == "True":
        enviado = True
    else:
        enviado = False
    try:
        track = Tracking.objects.get(trackNumber=trackNumber)
        track.clientName = clientName
        track.procesado = procesado
        track.armado = armado
        track.prueba = probado
        track.etiquetado = etiquetado
        track.enviado = enviado
        track.save()
    except Tracking.DoesNotExist:
        return JsonResponse({'status': 'Order not found'})
    return JsonResponse({'status': 'Order updated'})