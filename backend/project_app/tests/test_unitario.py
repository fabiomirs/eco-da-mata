from django.test import TestCase
from datetime import date
from project_app.models import Project
from community_app.models import Community

class projectTestCase(TestCase):
    def setUp(self):

        comunity = Community.objects.create(
            name = 'Comunidade de Teste',
            link = "https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
            latitude = -12.588229716430375,
            longitude = -55.739644976925305,
            description = 'Descrição da comunidade de teste',
            category ='COMMUNITY',
            logo = None
        )

        Project.objects.create(
            name = 'Teste',
            description = 'Teste Descrição',
            social_network_link = 'https://chat.openai.com',
            telephone_number = '7599252',
            email = 'test@gmail.com',
            community_key = comunity,
        )
    
    def test_project_create_correctly(self):
        project = Project.objects.get(name='Teste')
        self.assertEqual(project.description, 'Teste Descrição')

    def test_project_name_not_empty(self):
        project = Project.objects.get(name='Teste')
        self.assertNotEqual(project.name, '')
        self.assertIsNotNone(project.name)
        
    def test_project_descrption(self):
        project = Project.objects.get(name='Teste')
        self.assertEqual(project.description, 'Teste Descrição')
    
    def test_telephone_number(self):
        project = Project.objects.get(name='Teste')
        self.assertEqual(project.telephone_number, '7599252')
    
    def test_project_email(self):
        project = Project.objects.get(name='Teste')
        self.assertEqual(project.email, 'test@gmail.com')