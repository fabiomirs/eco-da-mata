from .models import People, Subcategory
from rest_framework import viewsets
from .serializers import PeopleSerializers, SubcategorySerializers

class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Subcategory.objects.all()
     serializer_class = SubcategorySerializers

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = People.objects.all()
     serializer_class = PeopleSerializers

