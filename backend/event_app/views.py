from .models import Event, Review
from rest_framework import viewsets
from .serializers import EventSerializers, ReviewSerializers

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
