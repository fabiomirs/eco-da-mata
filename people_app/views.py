from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import People
from .forms import PeopleForm
from django.views.generic.edit import UpdateView
from rest_framework import viewsets
from .serializers import PeopleSerializers




class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = People.objects.all()
     serializer_class = PeopleSerializers



class PeopleList(View):
    def get(self, request):
        people_list = get_list_or_404(People)
        
        return render(request, 'people_list.html', {'people_list': people_list})


class PeopleDetails(View):
    def get(request, pk):
        people = get_object_or_404(People, pk=pk)
        
        context = {"name": people.name,
                   "description": people.description,
                   "institutional_email": people.institutional_email,
                   "personal_page_link": people.personal_page_link,
                   "category": people.category
                   }
        return render(request, 'people_details.html', context)
    
    
    
    
class PeopleCreate(CreateView):
    template_name = "people_register.html"
    model = People
    form_class = PeopleForm
    success_url = reverse_lazy('people_list')
    
    
    
    
class PeopleUpdate(UpdateView):
    template_name = "people_update.html"
    model = People
    fields = ["name",
             "description",
            "institutional_email",
            "personal_page_link",
            "category",
            "subcategory_key"]

    
    
class PeopleDelete(DeleteView):
    template_name = "people_delete.html"
    model = People 
    context_object_name = 'pessoas'
    success_url = reverse_lazy("people_list")
    