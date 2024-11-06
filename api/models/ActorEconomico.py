from django.db import models
from .ActividadesEconomicas import ActividadEconomica
from .Denominacion import Denominacion
from .TipoMypime import TipoMypime
from .TipoSujeto import TipoSujeto
from .ActividadPrincipalCNAE import ActividadPrincipalCNAE
from .SectorEconomico import SectorEconomico
from django.contrib.auth.models import User
from .Origen import Origen
from .Solicitante import Solicitante

class ActorEconomico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    solicitud = models.CharField(max_length=11, null=False, blank=False)
    denominacion_id = models.ForeignKey(Denominacion,null=False, on_delete=models.CASCADE)
    tipo_sujeto_id = models.ForeignKey(TipoSujeto,null=False, on_delete=models.CASCADE)
    actividad_principal_CNAE_id = models.ForeignKey(ActividadPrincipalCNAE, related_name='actividad_principal_CNAE',null=False, on_delete=models.CASCADE)
    actividad_economica_principal_id = models.ForeignKey(ActividadEconomica,null=False, on_delete=models.CASCADE)
    solicitante_id = models.ForeignKey(Solicitante, on_delete=models.CASCADE, null=False)
    tipo_mypime_id = models.ForeignKey(TipoMypime,related_name="tipo_mipyme", on_delete=models.CASCADE, null=False)
    sector_economico_id= models.ForeignKey(SectorEconomico,related_name='sector_economico', null=False, on_delete=models.CASCADE)
    origen_id = models.ForeignKey(Origen, related_name='origen',null=False, default=None,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=11)
    correo_representante = models.EmailField()
    domicilio_social = models.CharField(max_length=250, null=False)
    cantidad_socios = models.IntegerField()
    cantidad_trabajadores = models.IntegerField()
    cantidad_estatales = models.IntegerField()
    cantidad_TPCP = models.IntegerField()
    cantidad_CNA = models.IntegerField()
    cantidad_desempleados = models.IntegerField()
    cantidad_otros_origenes = models.IntegerField()
    cantidad_ocupados = models.IntegerField()
    pdl = models.CharField(max_length=100)
    inscrito_registro_mercantil = models.BooleanField()
    tomo_inscripcion = models.CharField(max_length=10,null=False, blank=True)
    folio_inscripcion = models.CharField(max_length=10,null=False, blank=True)
    hoja_inscripcion = models.CharField(max_length=10,null=False, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True, null=True)
    is_exportador = models.BooleanField(default=False)
    is_incubado_en_parque_cientifico = models.BooleanField(default=False)
    desistimiento_con_carta_de_socios = models.BooleanField(default=False)
    is_disuelta = models.BooleanField(default=False)
    is_inactiva = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Actor Economico"
        verbose_name_plural = "Actores Economicos"
        db_table="backend.actores_economicos"
    def __str__(self):
        return self.nombre
    