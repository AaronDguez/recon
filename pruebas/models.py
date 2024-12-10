from django.db import models
from tracking.models import Tracking
from django.utils import timezone

# Create your models here.
class pruebas(models.Model):
    id = models.AutoField(primary_key=True)
    tamano = models.BooleanField(null=False),
    color = models.BooleanField(null=False),
    relleno = models.BooleanField(null=False),
    
    def to_dict(self) -> dict:
        return {
            'tamano': self.tamano,
            'color': self.color,
            'relleno': self.relleno
        }
    
    class Meta:
        db_table = 'pruebas'
        verbose_name = 'pruebas'
        verbose_name_plural = 'pruebas'