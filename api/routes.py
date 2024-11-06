from django.urls import path, include
from api.views.ActorEconomicoApiView import ActorEconomicoApiView
from api.views.SectorEconomicoAPIView import SectorEconomicoApiview
from api.views.TipoMipymeAPIView import TipoMypimeApiView
from api.views.TipoSujetoAPIView import TipoSujetoApiView
from api.views.DenominacionApiView import DenomacionAPIView
from api.views.ActividadPrincipalCNAEAPIView import ActividadPrincipalCNAEApiView
from api.views.ActividadEconominaAPIView import ActividadEconominaApiView
from api.views.LoginApiview import TokenRefreshView, CustomTokenObtainPairView
from api.views.RegisterApiview import RegisterView
from api.views.LogoutAPIView import LogoutView
from api.views.OrigenAPIView import OrigenApiView
from api.views.SolicitanteAPIView import SolicitanteApiView
from api.views.CargaDeDatos import CargarExcelAPIView
from api.views.Estadisticas import EstadisticasApiView

############################## ENDPOINTS ########################################

urlpatterns = (
    [
        ############ ACTORES ECONOMICOS #########################################
        path(
            "actorEconomico/obtenerActoresEconomicos/", ActorEconomicoApiView.as_view()
        ),
        path(
            'estadisticas/getEstadisticas/', EstadisticasApiView.as_view()
            ),
        path("actorEconomico/crearActorEconomico/", ActorEconomicoApiView.as_view(), name='crearActorEconomico'),
        path(
            "actorEconomico/obtenerActorEconomico/<int:pk>",
            ActorEconomicoApiView.as_view(),
        ),
        path(
            "actorEconomico/editarActorEconomico/<int:pk>",
            ActorEconomicoApiView.as_view(),
        ),
        path(
            "actorEconomico/eliminarActorEconomico/<int:pk>",
            ActorEconomicoApiView.as_view(),
        ),
    ]
    + [
        ################## TIPOS MYPIMES #############################
        path("tiposMiPymes/obtenerTiposMipymes/", TipoMypimeApiView.as_view()),
        path("tiposMiPymes/crearTipoMipyme/", TipoMypimeApiView.as_view()),
        path("tiposMiPymes/obtenerTipoMipyme/<int:id>", TipoMypimeApiView.as_view()),
        path("tiposMiPymes/editarTipoMipyme/<int:id>", TipoMypimeApiView.as_view()),
        path("tiposMiPymes/eliminarTipoMipyme/<int:id>", TipoMypimeApiView.as_view()),
    ]
    + [
        ################## SECTORES ECONOMICOS  #############################
        path(
            "sectorEconomico/obtenerSectoresEconomicos/",
            SectorEconomicoApiview.as_view(),
        ),
        path("sectorEconomico/crearSectorEconomico/", SectorEconomicoApiview.as_view()),
        path(
            "sectorEconomico/obtenerSectorEconomico/<int:id>",
            SectorEconomicoApiview.as_view(),
        ),
        path(
            "sectorEconomico/editarSectorEconomico/<int:id>",
            SectorEconomicoApiview.as_view(),
        ),
        path(
            "sectorEconomico/eliminarSectorEconomico/<int:id>",
            SectorEconomicoApiview.as_view(),
        ),
    ]
    + [
        ################# DENOMINACIONES ###############################
        path("denominaciones/obtenerDenominaciones/", DenomacionAPIView.as_view()),
        path("denominaciones/crearDenominacion/", DenomacionAPIView.as_view()),
        path(
            "denominaciones/obtenerDenominacion/<int:id>", DenomacionAPIView.as_view()
        ),
        path("denominaciones/editarDenominacion/<int:id>", DenomacionAPIView.as_view()),
        path(
            "denominaciones/eliminarDenominacion/<int:id>", DenomacionAPIView.as_view()
        ),
    ]
    + [
        ################ TIPOS SUJETOS #################################
        path("tiposSujetos/obtenerTiposSujetos/", TipoSujetoApiView.as_view()),
        path("tiposSujetos/crearTipoSujeto/", TipoSujetoApiView.as_view()),
        path("tiposSujetos/obtenerTipoSujeto/<int:id>", TipoSujetoApiView.as_view()),
        path("tiposSujetos/editarTipoSujeto/<int:id>", TipoSujetoApiView.as_view()),
        path("tiposSujetos/eliminarTipoSujeto/<int:id>", TipoSujetoApiView.as_view()),
    ]
    + [
        ################ ACTIVIDAD-PRINCIPAL-CNAE#########################
        path(
            "actividadPrincipal/obtenerActividadesPrincipalesCNAE/",
            ActividadPrincipalCNAEApiView.as_view(),
        ),
        path(
            "actividadPrincipal/obtenerActividadPrincipalCNAE/<int:pk>",
            ActividadPrincipalCNAEApiView.as_view(),
        ),
        path(
            "actividadPrincipal/crearActividadPrincipalCNAE/",
            ActividadPrincipalCNAEApiView.as_view(),
        ),
        path(
            "actividadPrincipal/editarActividadPrincipalCNAE/<int:pk>",
            ActividadPrincipalCNAEApiView.as_view(),
        ),
        path(
            "actividadPrincipal/eliminarActividadPrincipalCNAE/<int:pk>",
            ActividadPrincipalCNAEApiView.as_view(),
        ),
    ]
    + [
        ###################### ACTIVIDADES-ECONÓMICAS #######################
        path(
            "actividadEconomica/obtenerActividadesEconomicas/",
            ActividadEconominaApiView.as_view(),
        ),
        path(
            "actividadEconomica/obtenerActividadEconomicaPorCodigo/<str:code>",
            ActividadEconominaApiView.as_view(),
        ),
        path(
            "actividadEconomica/obtenerActividadEconomica/<int:pk>",
            ActividadEconominaApiView.as_view(),
        ),
        path(
            "actividadEconomica/crearActividadEconomica/",
            ActividadEconominaApiView.as_view(),
        ),
        path(
            "actividadEconomica/editarActividadEconomica/<int:pk>",
            ActividadEconominaApiView.as_view(),
        ),
        path(
            "actividadEconomica/eliminarActividadEconomica/<int:pk>",
            ActividadEconominaApiView.as_view(),
        ),
    ]
    + [
        ############################# USUARIOS #################################
        # path('auth/iniciarSesion/', LoginView.as_view()),
        # path('auth/registrarUsuario/', RegisterView.as_view()),
        # path('auth/cerrarSesion/', LogoutView.as_view()),
        path("auth/iniciarSesion/token/", CustomTokenObtainPairView.as_view()),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ]
    + [
        ########################### ORIGEN #######################################
        path("origen/obtenerOrigenes/", OrigenApiView.as_view()),
        path("origen/obtenerOrigen/<int:pk>", OrigenApiView.as_view()),
        path("origen/crearOrigenes/", OrigenApiView.as_view()),
        path("origen/editarOrigenes/<int:pk>", OrigenApiView.as_view()),
        path("origen/eliminarOrigenes/<int:pk>", OrigenApiView.as_view()),
    ]
    + [
        ############ SOLICITANTE ##############
        path("solicitante/obtenerSolicitantes/", SolicitanteApiView.as_view()),
        path("solicitante/obtenerSolicitante/<int:pk>", SolicitanteApiView.as_view()),
        path("solicitante/crearSolicitante/", SolicitanteApiView.as_view()),
        path("solicitante/editarSolicitante/<int:pk>", SolicitanteApiView.as_view()),
        path("solicitante/eliminarSolicitante/<int:pk>", SolicitanteApiView.as_view()),
    ]
    + [path("cargarExcel/", CargarExcelAPIView.as_view())]
)
