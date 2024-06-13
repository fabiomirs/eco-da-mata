from django.test import TestCase
from people_app.models import People, Subcategory


class PeopleTestCase(TestCase):
    def setUp(self):
        People.objects.create(
            name = 'Parceiro1',
            description = 'Parceiro eco-da-mata',
            institutional_email = 'test123@gmail.com',
            personal_page_link = 'http://linktest',
            logo = None,
            category = 'Instituição',
        )
    
        
    def test_people_create_sucess(self):
        people = People.objects.get(name = 'Parceiro1')
        self.assertEqual(people.description,'Parceiro eco-da-mata' )
        
        
    def test_nome_comunidade_nao_vazio(self):
        people = People.objects.get(name='Parceiro1')
        self.assertNotEqual(people.name, '')
        self.assertIsNotNone(people.name)
        
        
    def test_people_email(self):
        people = People.objects.get(name='Parceiro1')
        self.assertEqual(people.institutional_email,'test123@gmail.com' )
      
        
    def test_people_category(self):
        people = People.objects.get(name='Parceiro1')
        self.assertIn(people.category,['Instituição', 'Pessoa Fisica'])
        
        
        
