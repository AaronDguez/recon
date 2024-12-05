from django.db import models
from django.utils import timezone

# Create your models here.
class Material(models.Model):
    materiales = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    codigo_barras = models.CharField(max_length=12, unique=True, null=True, blank=True)
    
    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
    
    def __str__(self) -> str:
        return self.materiales
    
class ActualizacionInventario(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    codigo_barras = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'actualizacion_inventario'
        verbose_name = 'Actualización de Inventario'
        verbose_name_plural = 'Actualizaciones de Inventario'
    
    def __str__(self) -> str:
        return self.material.materiales