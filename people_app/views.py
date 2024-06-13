from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import People, Subcategory
from .forms import PeopleForm, SubcategoryForm
from django.views.generic.edit import UpdateView
from rest_framework import viewsets
from .serializers import PeopleSerializers, SubcategorySerializers



class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Subcategory.objects.all()
     serializer_class = SubcategorySerializers
    



class SubcategoryList(View):
    def get(self, request):
        subcategory_list = get_list_or_404(Subcategory)
        
        return render(request, 'subcategory_list.html', {'subcategory_list': subcategory_list})



class UniqueSubcategory(View):
    def get(request, pk):
        subcategory = get_object_or_404(Subcategory, pk=pk)
        
        context = {"title": subcategory.title,
                   "category": subcategory.category
                   }
        
        return render(request, 'subcategory_unique.html', context)
    
    
    
class SubcategoryCreate(CreateView):
    template_name = "subcategory_register.html"
    model = Subcategory
    form_class = SubcategoryForm
    success_url = reverse_lazy('subcategory_list')
    
    
    
class  SubcategoryUpdate(UpdateView):
    template_name = "subcategory_update.html"
    model = Subcategory
    fields = ["title",
            "category"
    ]
    
    
    
class SubcategoryDelete(DeleteView):
    template_name = "subcategory_delete.html"
    model = Subcategory
    context_object_name = 'subcategoria'
    success_url = reverse_lazy("subcategory_list")    





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
    