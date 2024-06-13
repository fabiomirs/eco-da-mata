from django.urls import path
from .views import *

urlpatterns = [
    path('all/', EventList.as_view(), name='event-list'),
    path('<int:pk>/', DetailedEvent.as_view(), name='detailed-event'),
    path('create/', EventCreation.as_view(), name='create-event'),
    path('<int:pk>/update/', EventUpdate.as_view(), name='update-event'),
    path('<int:pk>/delete/', EventDeletion.as_view(), name='delete-event'),
]
