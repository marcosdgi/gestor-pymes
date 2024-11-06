from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
from django.db.models import Count, Q, Sum
from django.db.models.functions import ExtractMonth
from api.models.ActorEconomico import (
    ActorEconomico,
)  # Asegúrate de importar tus modelos
import calendar
from api.models.Solicitante import Solicitante


class EstadisticasApiView(APIView):
    def get(self, request):
        # Contadores de actores con campos específicos en True
        stats_actores = {
            "exportadores": ActorEconomico.objects.filter(is_exportador=True).count(),
            "incubados_en_parque": ActorEconomico.objects.filter(
                is_incubado_en_parque_cientifico=True
            ).count(),
            "con_desistimiento": ActorEconomico.objects.filter(
                desistimiento_con_carta_de_socios=True
            ).count(),
            "disueltos": ActorEconomico.objects.filter(is_disuelta=True).count(),
            "inactivos": ActorEconomico.objects.filter(is_inactiva=True).count(),
        }

        # Obtener los parámetros de año y mes de la solicitud
        year = request.GET.get("year")
        mes = request.GET.get("mes")

        # Filtrar los actores económicos creados por año y opcionalmente por mes
        if year:
            if mes:  # Si también se proporciona el mes
                created_by_month = (
                    ActorEconomico.objects.filter(
                        created_at__year=year, created_at__month=mes
                    )
                    .values("created_at__year", "created_at__month")
                    .annotate(count=Count("id"))
                )
            else:  # Solo se proporciona el año
                created_by_month = (
                    ActorEconomico.objects.filter(created_at__year=year)
                    .annotate(month=ExtractMonth("created_at"))
                    .values("month")
                    .annotate(count=Count("id"))
                    .order_by("month")
                )
        else:
            created_by_month = []

        # Contadores de actores económicos con y sin relación a solicitante
        actores_con_solicitante = ActorEconomico.objects.filter(
            solicitante_id__isnull=False
        ).count()
        actores_sin_solicitante = ActorEconomico.objects.filter(
            solicitante_id__isnull=True
        ).count()
        solicitantes = Solicitante.objects.all().count()

        # Sumar el total de trabajadores
        total_trabajadores = (
            ActorEconomico.objects.aggregate(total=Sum("cantidad_trabajadores"))[
                "total"
            ]
            or 0
        )

        # Preparar los datos de respuesta
        response_data = {
            "statsActores": stats_actores,
            "totalTrabajadores": total_trabajadores,
            "createdByMonth": created_by_month,
            "actoresRelacionSolicitante": {
                "solicitantes": solicitantes,
                "con_solicitante": actores_con_solicitante,
                "sin_solicitante": actores_sin_solicitante,
            },
        }

        return Response(response_data)
