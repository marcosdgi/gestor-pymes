from django_filters import FilterSet
from api.models.ActorEconomico import ActorEconomico

class ActorEconomicoFilter(FilterSet):
    class Meta:
        model = ActorEconomico
        fields = [
            "nombre",
            "solicitud",
            "denominacion_id",
            "tipo_sujeto_id",
            "actividad_principal_CNAE_id",
            "actividad_economica_principal_id",
            "solicitante_id",
            "tipo_mypime_id",
            "sector_economico_id",
            "origen_id",
            "tomo_inscripcion",
            "folio_inscripcion",
            "is_exportador",
            "is_incubado_en_parque_cientifico",
            "is_disuelta",
            "is_inactiva"            
        ]