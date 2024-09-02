from django.db import models


class TipoSujeto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Tipo Sujeto"
        verbose_name_plural = "Tipos Sujetos"
        db_table="backend.tipo_sujeto"
    def __str__(self):
        return self.nombre