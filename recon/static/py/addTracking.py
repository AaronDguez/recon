from tracking.models import Tracking
from inventario.models import Material, ActualizacionInventario
from django.http import JsonResponse
import time
import random

"""
    This function creates a new order in the database.
    trackData: dict - Dictionary with the order data from the form.
"""
def addTracking(trackData:dict):
    year: int = time.localtime().tm_year
    week: int = time.localtime().tm_yday // 7
    # Generate a unique track number with the format MYYYYWWXXX where:
    # M is for it being manufactured in Mexico.
    # YYYY is the year and WW is the week of the year where it was created.
    # XXX is a 3 digit number that is unique for each order. Its supposed to be a consecutive number, but for the sake of this project, it will be random.
    trackNumberExists: bool = True
    while trackNumberExists:
        numericOrder: int = random.randint(1, 999) # Random number between 1 and 999.
        trackNumber = f"M{year}{week}{numericOrder:03}" # Format the track number.
        trackNumberExists = Tracking.objects.filter(trackNumber=trackNumber).exists() # Check if the track number already exists.
    # Get order from the form and prepare it for the database.
    quantityBoxes: int = int(trackData.get('quantityBoxes'))
    clientName: str = trackData.get('orderName')
    track = Tracking(trackNumber=trackNumber, clientName=clientName)
    # Check if there is enough material to create the order.
    if checkMaterial(quantityBoxes):
        try:
            track.save()
        except Exception as e:
            # If there is an error related to the database, return an error message.
            return JsonResponse({'status': f'Error adding order, {e}'})
        return JsonResponse({'status': 'Order added'})
    else:
        # If there the Material table is empty, return an error message.
        return JsonResponse({'status': 'Material not found'})

"""
    This function checks if there is enough material to create the order.
    quantity: int - Quantity of boxes to create.
"""
def checkMaterial(quantity:int):
    try:
        Materiales = Material.objects.all()
        # If there are no materials in the database, throw an exception.
        if not Materiales:
            raise Material.DoesNotExist
        for material in Materiales:
            if material.materiales == 'Caja':
                if material.cantidad < quantity:
                    # If there is not enough boxes, place a purchase order for the missing boxes, but for the sake of this project, just add the boxes.
                    nuevoLog = ActualizacionInventario(material=material, cantidad=quantity)
                    materialActualizado = Material.objects.get(materiales='Caja')
                    materialActualizado.cantidad += quantity
                    materialActualizado.save()
                    nuevoLog.save()
                # Subtract the quantity of boxes from the inventory.
                nuevoLog = ActualizacionInventario(material=material, cantidad=(-quantity))
                materialActualizado = Material.objects.get(materiales='Caja')
                materialActualizado.cantidad -= quantity
                materialActualizado.save()
                nuevoLog.save()
                # Go to the next material, and repeat for the rest of the materials.
                next
            elif material.materiales == 'Cinta':
                if material.cantidad < quantity * 100: # 100 cm of tape per box.
                    # Simulate purchase of tape.
                    nuevoLog = ActualizacionInventario(material=material, cantidad=(quantity * 100))
                    materialActualizado = Material.objects.get(materiales='Cinta')
                    materialActualizado.cantidad += quantity * 100
                    materialActualizado.save()
                    nuevoLog.save()
                # Subtract the quantity of tape from the inventory.
                nuevoLog = ActualizacionInventario(material=material, cantidad=(-quantity * 100))
                materialActualizado = Material.objects.get(materiales='Cinta')
                materialActualizado.cantidad -= quantity * 100
                materialActualizado.save()
                nuevoLog.save()
                next
            elif material.materiales == 'Etiqueta':
                if material.cantidad < quantity:
                    # Simulate purchase of labels.
                    nuevoLog = ActualizacionInventario(material=material, cantidad=quantity)
                    materialActualizado = Material.objects.get(materiales='Etiqueta')
                    materialActualizado.cantidad += quantity
                    materialActualizado.save()
                    nuevoLog.save()
                # Subtract the quantity of labels from the inventory.
                nuevoLog = ActualizacionInventario(material=material, cantidad=(-quantity))
                materialActualizado = Material.objects.get(materiales='Etiqueta')
                materialActualizado.cantidad -= quantity
                materialActualizado.save()
                nuevoLog.save()
                break # This is the last material, so break the loop.
        return True
    except Material.DoesNotExist:
        return False
