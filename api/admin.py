from django.contrib import admin
from .models.ActividadesEconomicas import ActividadEconomica
from .models.ActividadPrincipalCNAE import ActividadPrincipalCNAE
from .models.ActorEconomico import ActorEconomico
from .models.Denominacion import Denominacion
from .models.TipoMypime import TipoMypime
from .models.TipoSujeto import TipoSujeto
from .models.SectorEconomico import SectorEconomico
from .models.Origen import Origen
from .models.Solicitante import Solicitante

#############################ADMIN#################################
admin.site.register(ActividadEconomica)
admin.site.register(ActividadPrincipalCNAE)
admin.site.register(ActorEconomico)
admin.site.register(Denominacion)
admin.site.register(TipoMypime)
admin.site.register(TipoSujeto)
admin.site.register(SectorEconomico)
admin.site.register(Solicitante)
admin.site.register(Origen)