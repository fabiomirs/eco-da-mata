from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event, Review
from .forms import EventForm
from rest_framework import viewsets
from .serializers import EventSerializers, ReviewSerializers

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
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
    pk_url_kwarg = 'pk'


class EventCreation(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_creation.html'
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('detailed-event', kwargs={'pk': pk})


class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_update.html'

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('detailed-event', kwargs={'pk': pk})


class EventDeletion(DeleteView):
    model = Event
    template_name = 'event_deletion.html'
    success_url = reverse_lazy('event-list')

