from django.test import TestCase
from people_app.models import People, Subcategory


class PeopleTestCase(TestCase):
  
    
    def setUp(self):
        subcategory = Subcategory.objects.create(title='Subcategoria de teste')
        People.objects.create(
            name = 'Parceiro1',
            description = 'Parceiro eco-da-mata',
            institutional_email = 'test123@gmail.com',
            personal_page_link = 'http://linktest',
            logo = None,
            category = 'Instituição',
            subcategory_key = subcategory
        )
    
        
    def test_people_create_success(self):
        people = People.objects.get(name = 'Parceiro1')
        self.assertEqual(people.description,'Parceiro eco-da-mata' )
        
        
    def test_people_name(self):
        people = People.objects.get(name='Parceiro1')
        self.assertNotEqual(people.name, '')
        self.assertIsNotNone(people.name)
        
        
    def test_people_email(self):
        people = People.objects.get(name='Parceiro1')
        self.assertEqual(people.institutional_email,'test123@gmail.com' )
      
        
    def test_people_category(self):
        people = People.objects.get(name='Parceiro1')
        self.assertIn(people.category,['Instituição', 'Pessoa Fisica'])
        
        
        
class SubcategoryTestCase(TestCase):
    def setUp(self):
        People.objects.create(
        title = 'teste subcategoria',
        category = 'Pessoa fisica'
        )
        
        
    def test_subcategory_name(self):
        subcategory = Subcategory.objects.get(title='teste subcategoria')
        self.assertNotEqual(subcategory.title, '')
        self.assertIsNotNone(subcategory.title)
        
        
    def test_subcategory_category(self):
        subcategory= Subcategory.objects.get(title='teste subcategoria')
        self.assertIn(subcategory.category,['Instituição', 'Pessoa Fisica'])
    
        
    