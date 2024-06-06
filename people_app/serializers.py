from rest_framework import serializers
from .models import People

class PeopleSerializers(serializers.ModelSerializer):
    class Meta():
        model = People
        fields = '__all__'