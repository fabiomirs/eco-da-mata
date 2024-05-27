from django import forms
from .models import Subcategory


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['title', 'category']
        widgets = {'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
                   'category': forms.Select(choices=[('institution', 'Instituição'), ('physical_person', 'Pessoa Física')])
                   }
       