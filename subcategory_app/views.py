from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import SubcategoryForm
from .models import Subcategory 


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
    
    
    
class PeopleCreate(CreateView):
    template_name = "people_register.html"
    model = Subcategory
    form_class = SubcategoryForm
    success_url = reverse_lazy('subcategory_list')
    

    
    

    