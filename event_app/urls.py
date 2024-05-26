from django.urls import path
from .views import EventList, DetailedEvent, EventCreation

urlpatterns = [
    path('all/', EventList.as_view(), name='event-list'),
    path('all/<int:event_id>/', DetailedEvent.as_view(), name='detailed-event'),
    path('create', EventCreation.as_view(), name='create-event'),
]
