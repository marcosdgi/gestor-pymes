from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from api.models import ActorEconomico


class ActorEconomicoAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(
            "crearActorEconomico"
        )  # Asegúrate de que este nombre coincide con el registrado en routes.py

    def test_create_actor_economico(self):
        data = {
            " solicitud": "23094",
            " denominacion_id": 1,
            "actividad_economica_principal_id": 1,
            "actividad_principal_CNAE_id": 1,
            "cantidad_CNA": 1,
            "cantidad_TPCP": 1,
            "cantidad_desempleados": 1,
            "cantidad_estatales": 1,
            "cantidad_ocupados": 1,
            "cantidad_otros_origenes": 1,
            "cantidad_socios": 1,
            "cantidad_trabajadores": 1,
            "correo_representante": "fsfdf@gmail.com",
            "denominacion_id": 1,
            "desistimiento_con_carta_de_socios": False,
            "domicilio_social": "fsdfsdf",
            "fecha_incripcion": "2024-11-20",
            "folio_inscripcion": "sdfsdf",
            "hoja_inscripcion": "sdfsfd",
            "inscrito_registro_mercantil": False,
            "is_disuelta": False,
            "is_exportador": False,
            "is_inactiva": True,
            "is_incubado_en_parque_cientifico": True,
            "nombre": "Data",
            "numero": 1,
            "origen_id": 1,
            "pdl": "sdfsdf",
            "sector_economico_id": 1,
            "solicitante_id": 2,
            "solicitud": "23094",
            "telefono": "3424234",
            "tipo_mypime_id": 1,
            "tipo_sujeto_id": 1,
        }

        response = self.client.post(self.url, data, format="json")
        print(response.data)  # Añade esta línea para imprimir los errores de validación
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ActorEconomico.objects.count(), 1)
        self.assertEqual(ActorEconomico.objects.get()
                         )

    def test_create_actor_economico_invalid(self):
        data = {"nombre": ""}

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
