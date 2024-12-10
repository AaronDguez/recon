from django.db import models

# Create your models here.
class pruebas(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False),
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