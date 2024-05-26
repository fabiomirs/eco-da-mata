from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Event
from .forms import EventCreationForm

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


class EventCreation(CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event_creation.html'
    success_url = '/eventos/all/'

