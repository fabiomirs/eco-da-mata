from rest_framework import serializers
from .models import People, Subcategory

class PeopleSerializers(serializers.ModelSerializer):
    class Meta():
        model = People
        fields = '__all__'
        

class SubcategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = Subcategory
        fields = '__all__'