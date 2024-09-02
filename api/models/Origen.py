from django.db import models


class Origen(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Origen'
        verbose_name_plural = 'Origenes'
        db_table="backend.origen"
    def __str__(self):
        return self.nombre