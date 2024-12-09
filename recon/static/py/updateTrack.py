from tracking.models import Tracking
from django.http import JsonResponse

def updateTrack(trackData:dict):
    """This function updates the status of an order in the database

    Args:
        trackData (dict): Dictionary with the order information.

    Returns:
        JsonResponse: {"status": "Order updated"} if the order was updated successfully, {"status": "Order not found"} if the order was not found.
    """
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