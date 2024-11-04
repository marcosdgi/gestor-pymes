from django.db import models
from .TipoMypime import TipoMypime

class Solicitante( models.Model ):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    segundo_nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=False)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=False)
    correo = models.EmailField(null=True)
    carnet = models.CharField(max_length=11, null=False)
    fecha_nacimiento = models.DateField(null=False, default=None)
    genero = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=100, null=False)
    tipo_mipyme_id = models.ForeignKey(TipoMypime, related_name='tipo_mipyme_en_posecion', null=False, on_delete=models.CASCADE)
    tomo = models.CharField(max_length=3, null=False)
    folio = models.CharField(max_length=3, null=False)

    class Meta:
        verbose_name = 'Solicitante'    
        verbose_name_plural = 'Solicitantes'
        db_table="backend.solicitante"
    def __str__(self):
        if self.segundo_nombre is not None:
            return self.apellido_paterno + ' ' + self.apellido_materno + ' ' + self.nombre + ' ' + self.segundo_nombre
        else:
            return self.apellido_paterno + ' ' + self.apellido_materno + ' ' + self.nombre