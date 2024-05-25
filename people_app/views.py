from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import People
from django.views import View


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
    
    

    