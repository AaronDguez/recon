from tracking.models import Tracking
from inventario.models import Material, ActualizacionInventario
from django.http import JsonResponse

def addTracking(trackData:dict):
    trackNumber = trackData.get('trackNumber')
    quantityBoxes = trackData.get('quantityBoxes')
    clientName = trackData.get('orderName')
    track = Tracking(trackNumber=trackNumber, clientName=clientName)
    if checkMaterial(quantityBoxes):
        try:
            track.save()
        except Exception as e:
            return JsonResponse({'status': f'Error adding order, {e}'})
        return JsonResponse({'status': 'Order added'})
    else:
        return JsonResponse({'status': 'Material not found'})

    
def checkMaterial(quantity:int):
    try:
        Materiales = Material.objects.all()
        for material in Materiales:
            if material.name == 'Caja':
                if material.quantity < quantity:
                    pass # Actualizar la cantidad de cajas como si se hubieran comprado mas
                # Actualizar el historial de inventario restando la cantidad de cajas.
                
                # Ir al siguiente material.
                
            elif material.name == 'Cinta':
                if material.quantity < quantity * 100: # 100 cm de cinta por caja
                    pass # Actualizar la cantidad de tape como si se hubieran comprado mas
                # Actualizar el historial de inventario restando la cantidad de tape.
                
                # Ir al siguiente material.
                
            elif material.name == 'Etiqueta':
                if material.quantity < quantity:
                    pass # Actualizar la cantidad de etiquetas como si se hubieran comprado mas
                # Actualizar el historial de inventario restando la cantidad de etiquetas.
                
                break # No hay mas materiales que verificar.        
        
        return True
    except Material.DoesNotExist:
        return False
