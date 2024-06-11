from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from rest_framework import status
from community_app.models import Community
from community_app.serializers import CommunitySerializer
from datetime import date

class CommunityIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.community = Community.objects.create(
            name='Comunidade de Teste',
            link="https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
            latitude=-12.588229716430375,
            longitude=-55.739644976925305,
            description='Descrição da comunidade de teste',
            category='COMMUNITY',
            logo=None
        )

    def test_ler_comunidade_via_get(self):
        url = reverse('community-detail', kwargs={'pk': self.community.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifique se os dados retornados correspondem aos dados da comunidade criada
        serializer = CommunitySerializer(self.community)
        self.assertEqual(response.data, serializer.data)