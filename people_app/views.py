from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import People
from .forms import PeopleForm

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
        return render(request, 'people_detail.html', context)
    
    
    
class PeopleCreate(CreateView):
    template_name = "register_people.html"
    model = People
    form_class = PeopleForm
    success_url = reverse_lazy('people_list')
    
    

    