from rest_framework import serializers
from .models import Subcategory

class SubcategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = Subcategory
        fields = '__all__'