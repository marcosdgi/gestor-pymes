from django.db import models



class ActividadPrincipalCNAE (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    
    class Meta:
        verbose_name="Actividad CNAE"
        db_table="backend.actividad_principal_cnae"
    def __str__(self):
        return self.nombre