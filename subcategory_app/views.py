from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import SubcategoryForm
from .models import Subcategory 
from rest_framework import viewsets
from .serializers import SubcategorySerializers




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
    

    
    
    
    

    
    

    