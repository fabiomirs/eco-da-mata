from django.test import TestCase
from community_app.models import Community
from datetime import date

class CommunityTestCase(TestCase): 
    def setUp(self):
        Community.objects.create(
            name = 'Comunidade de Teste',
            link = "https://maps.app.goo.gl/pahfS5uhEWR2XJN97",
            latitude = -12.588229716430375,
            longitude = -55.739644976925305,
            description = 'Descrição da comunidade de teste',
            category ='COMMUNITY',
            logo = None
        )
    
    def test_comunidade_criada_com_sucesso(self):
        comunidade = Community.objects.get(name='Comunidade de Teste')
        self.assertEqual(comunidade.description, 'Descrição da comunidade de teste')

    def test_latitude_da_comunidade(self):
        comunidade = Community.objects.get(name='Comunidade de Teste')
        self.assertAlmostEqual(comunidade.latitude, -12.588229716430375, delta=0.1)

    def test_longitude_da_comunidade(self):
        comunidade = Community.objects.get(name='Comunidade de Teste')
        self.assertAlmostEqual(comunidade.longitude, -55.739644976925305, delta=0.1)
    
    def test_categoria_comunidade(self):
        comunidade = Community.objects.get(name='Comunidade de Teste')
        self.assertIn(comunidade.category, ['COMMUNITY','TOURIST_SPOT'])
    
    def test_nome_comunidade_nao_vazio(self):
        comunidade = Community.objects.get(name='Comunidade de Teste')
        self.assertNotEqual(comunidade.name, '')
        self.assertIsNotNone(comunidade.name)
