from django.views import View
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Event

# Create your views here.
class RegisteredEvents(View):
    def get(self, request):
        events = get_list_or_404(Event)

        return render(request, 'event_list.html', {'events' : events})

class SingleEvent(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)

        return render(request, 'detailed_event.html', {'event' : event})