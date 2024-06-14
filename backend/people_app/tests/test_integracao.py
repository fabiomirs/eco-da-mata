from django.urls import reverse
from django.test import TestCase
from people_app.models import People, Subcategory
from rest_framework import status
from django.test.client import Client

class PeopleSubcategoryIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        subcategory = Subcategory.objects.create(title='Subcategoria de teste', category='institution')
        self.people = People.objects.create(
            name='Parceiro1',
            description='Parceiro eco-da-mata',
            institutional_email='test123@gmail.com',
            personal_page_link='http://linktest',
            logo=None,
            category='institution',
            subcategory_key=subcategory
        )

    def test_create_people_by_post(self):
        url = reverse('people-detail', kwargs={'pk': self.people.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    