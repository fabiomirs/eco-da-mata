from rest_framework import serializers
from .models import Event, Review

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

