from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'description', 'institutional_email', 'personal_page_link', 'logo', 'category']
        widgets = {'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
                   'institutional_email': forms.EmailInput(),
                   'personal_page_link': forms.URLInput(),
                   'logo': forms.ClearableFileInput(),
                   'category': forms.Select(choices=[('institution', 'Instituição'), ('physical_person', 'Pessoa Física')])
                   }
       
       