from django.db import models

# Create your models here.
class Tracking(models.Model):
    trackNumber = models.CharField(primary_key=True, max_length=10, null=False, unique=True)
    clientName = models.CharField(max_length=50, null=False)
    procesado = models.BooleanField(null=True, blank=True, default=None)
    armado = models.BooleanField(null=True, blank=True, default=None)
    prueba = models.BooleanField(null=True, blank=True, default=None)
    etiquetado = models.BooleanField(null=True, blank=True, default=None)
    enviado = models.BooleanField(null=True, blank=True, default=None)

    def to_dict(self) -> dict:
        return {
            'trackNumber': self.trackNumber,
            'clientName': self.clientName,
            'procesado': self.procesado,
            'armado': self.armado,
            'prueba': self.prueba,
            'etiquetado': self.etiquetado,
            'enviado': self.enviado
        }
    
    class Meta:
        db_table = 'tracking'
        verbose_name = 'Tracking'
        verbose_name_plural = 'Trackings'
        ordering = ['trackNumber']