from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from event_app.models import Event
from datetime import date
from rest_framework import status
from event_app.serializers import EventSerializers
from project_app.models import Project
from community_app.models import Community

class EventIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        comunity = Community.objects.create(
            name = 'Comunidade de Teste',
            link = "https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
            latitude = -12.588229716430375,
            longitude = -55.739644976925305,
            description = 'Descrição da comunidade de teste',
            category ='COMMUNITY',
            logo = None
        )

        project = Project.objects.create(
            name = 'Teste',
            description = 'Teste Descrição',
            social_network_link = 'https://chat.openai.com',
            telephone_number = '7599252',
            email = 'test@gmail.com',
            community_key = comunity,
        )

        self.event = Event.objects.create(
            name='Evento Teste',
            start_date=date.today(),
            end_date=date.today(),
            time= '10:00',
            description= 'Descrição Evento',
            category= 'LC',
            address = 'Rua para teste, 777',
            location= 'Casa da arvore de teste',
            link= 'https://chat.openai.com',
            format= 'IP',
            value= 100.00, 
            pix_key= '75-992502518',
            pix_key_owner= 'Guilherme Fernandes',
            bank_name= 'Nubank',
            pdf_link= 'http://www.prograd.uefs.br/arquivos/File/Calendario/2024/Resolucaoconsepe1652023calendario20241.pdf',
            questionary_link= 'https://docs.google.com/forms/d/e/1FAIpQLSdYLB5zwBzrHQWkHoVhhVGIHfr5H1mCJfqT6HG4-t-wQO03xg/alreadyresponded',
            profile_picture = None,
            project_FK = project,
            )

    def test_create_event_by_post(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    