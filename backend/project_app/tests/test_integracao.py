from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from rest_framework import status
from project_app.serializers import ProjectSerializer
from project_app.models import Project
from community_app.models import Community

class ProjectIntegrationTestCase(TestCase):
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

        self.project = Project.objects.create(
            name = 'Teste',
            description = 'Teste Descrição',
            social_network_link = 'https://chat.openai.com',
            telephone_number = '7599252',
            email = 'test@gmail.com',
            community_key = comunity,
        )

    def test_create_project_by_post(self):
        url = reverse('project-detail', kwargs={'pk': self.project.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)