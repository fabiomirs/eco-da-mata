from django.urls import path
from .views import EventList, DetailedEvent

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('<int:event_id>/', DetailedEvent.as_view(), name='detailed-event'),
]
