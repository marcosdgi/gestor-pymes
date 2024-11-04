from django.db import models


class TipoMypime(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Tipo Mypime'
        verbose_name_plural = 'Tipos Mypimes'
        db_table="backend.tipo_mipyme"
    def __str__(self):
        return self.nombre