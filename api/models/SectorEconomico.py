from django.db import models


class SectorEconomico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, blank=False, max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Sector Economico"
        verbose_name_plural = "Sectores Economicos"
        db_table="backend.sector_economico"
    def __str__(self):
        return self.nombre