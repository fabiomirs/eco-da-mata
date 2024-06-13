from django.test import TestCase
from event_app.models import Event
from datetime import date
from project_app.models import Project
from community_app.models import Community

class EventTestCase(TestCase):
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

        project = Project.objects.create(
            name = 'Teste',
            description = 'Teste Descrição',
            social_network_link = 'https://chat.openai.com',
            telephone_number = '7599252',
            email = 'test@gmail.com',
            community_key = comunity,
        )

        Event.objects.create(
            name='Evento Teste',
            start_date=date.today(),
            end_date=date.today(),
            time= '10:00',
            description= 'Descrição Evento para teste',
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
    
    def test_event_create_correctly(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertEqual(event.description, 'Descrição Evento para teste')
    
    def test_event_value(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertAlmostEqual(float(event.value), 100.00, delta=0.02)

    def test_event_format(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertIn(event.format, ['IP', 'In person', 'ON', 'Online', 'HB', 'Hybrid'])

    def test_end_date_after_start_date(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertGreaterEqual(event.end_date, event.start_date)

    def test_event_name_not_empty(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertNotEqual(event.name, '')
        self.assertIsNotNone(event.name)

    def test_event_category(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertIn(event.category, ['LC', 'Lecture', 'FR', 'Fair', 'CF', 'Conference', 'WK', 'Workshop', 'SM', 'Seminary' ,
     'AE', 'Art Exhibition', 'FV', 'Festival', 'OT', 'Others'])
        
    def test_event_address_location(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertEqual(event.address, 'Rua para teste, 777')
        self.assertEqual(event.location, 'Casa da arvore de teste')
    
    def test_pix_and_bank(self):
        event = Event.objects.get(name='Evento Teste')
        self.assertEqual(event.pix_key, '75-992502518')
        self.assertEqual(event.pix_key_owner, 'Guilherme Fernandes')
        self.assertEqual(event.bank_name, 'Nubank')