from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from community_app.models import Community
from datetime import date

class CommunityIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Community.objects.create(
            name = 'Comunidade de Teste',
            link = "https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
            latitude = -12.588229716430375,
            longitude = -55.739644976925305,
            description = 'Descrição da comunidade de teste',
            category ='COMMUNITY',
            logo = None
        )

        def test_ler_evento_via_get(self):
            url = reverse('api/community')
            response = self.clien.get(url,{
                'name' : 'Comunidade de Teste',
                'link' : "https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
                'latitude' : -12.588229716430375,
                'longitude' : -55.739644976925305,
                'description' : 'Descrição da comunidade de teste',
                'category' :'COMMUNITY',
                'logo' : None
            })

            self.assertEqual(response.status_code, 200)
            nova_comunidade = Community.objects.get(nome='Comunidade de Teste')
            self.assertIsNotNone(nova_comunidade)
