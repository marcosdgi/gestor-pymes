from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from api.models.TipoSujeto import TipoSujeto
from api.models.ActividadesEconomicas import ActividadEconomica
from api.models.ActividadPrincipalCNAE import ActividadPrincipalCNAE
from api.models.Denominacion import Denominacion
from api.models.SectorEconomico import SectorEconomico
from api.models.TipoMypime import TipoMypime
from api.models.ActorEconomico import ActorEconomico
from .serializers import ActorEconomicoSerializer

class CargarExcelAPIView(APIView):
    ###################### REVISAR LOS DATOS Y LA MANERA EN QUE ENTRAN ESTOS DATOS ######################################
    def post(self, request, *args, **kwargs):
        archivo_excel = request.FILES.get('archivo')
        if not archivo_excel:
            return Response({"error": "No se ha proporcionado un archivo"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_excel(archivo_excel)
            for _, row in df.iterrows():
                datos = {
                    'nombre': row['Nombre'],
                    'numero': row['No'],
                    'tipo_mypime_id': TipoMypime.objects.get(nombre=row['TipoMypime']).id,
                    'denominacion_id': Denominacion.objects.get(nombre=row['Denominacion']).id,
                    'tipo_sujeto_id': TipoSujeto.objects.get(nombre=row['TipoSujeto']).id,
                    'actividad_economica_principal_id': ActividadPrincipalCNAE.objects.get(nombre=row['ActividadPrincipalCNAE']).id,
                    'sector_economico_id': SectorEconomico.objects.get(nombre=row['SectorEconomico']).id,
                    'actividad_principal_CNAE_id': ActividadEconomica.objects.get(nombre=row['ActividadPrincipalCNAE']).id,
                    'solicitud': row['Solicitud'],
                    'telefonos': row['Telefonos'],
                    'correo_representante': row['Correo del Representante'],
                    'domicilio': row['Domicilio Social'],
                    'cantidad_socios': row['Cantidad de Socios'],
                    'cantidad_trabajadores': row['Cantidad de Trabajadores'],
                    'cantidad_estatales': row['Cantidad Estatales'],
                    'cantidad_TPCP': row['Cantidad TPCP'],
                    'cantidad_CNA': row['Cantidad CNA'],
                    'cantidad_desempleados': row['Cantidad Desempleados'],
                    'cantidad_otros_origenes': row['Cantidad otros orígenes'],
                    'cantidad_ocupados': row['Cantidad de Ocupados'],
                    'is_exportador': row['Exporta'],
                    'is_disuelta': row['Disuelta'],
                    # 'is_inactiva': row['Disuelta'],
                    'is_incubado_en_parque_cientifico': row['Siendo incubado en un parque cientifico y tecnológico'],
                    'desistimiento_con_carta_de_socios': row['Desistimiento con carta de los socios y sin carta'],
                    'pdl':row['PDL'],
                    'origen_id': row['Origen']
                }
                serializer = ActorEconomicoSerializer(data=datos)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"mensaje": "Datos cargados exitosamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
