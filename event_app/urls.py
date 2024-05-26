from django.urls import path
from .views import EventList, DetailedEvent, EventCreation, EventUpdate

urlpatterns = [
    path('all/', EventList.as_view(), name='event-list'),
    path('all/<int:pk>/', DetailedEvent.as_view(), name='detailed-event'),
    path('create/', EventCreation.as_view(), name='create-event'),
    path('update/<int:pk>/', EventUpdate.as_view(), name='update-event')
]
