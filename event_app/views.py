from django.views import View
from django.views.generic import ListView, DetailView
from .models import Event

# Create your views here.
class EventList(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'      
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all().order_by('start_date')

class DetailedEvent(DetailView):
    model = Event
    template_name = 'detailed_event.html'  
    context_object_name = 'event'          
    pk_url_kwarg = 'event_id'