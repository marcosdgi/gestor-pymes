from django.db import models


class ActividadEconomica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    codigo = models.CharField(max_length=10, blank=False, null=False,  default=0000)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name="Actividad Economica"
        verbose_name_plural = "Actividades Economicas"
        db_table = 'backend.actividad_economica'
    def __str__(self):
        return self.nombre