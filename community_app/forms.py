from django import forms
from .models import Community, News

class CreateCommunityForm(forms.ModelForm):
    class Meta: 
        model = Community
        fields = ['name', 'link', 'latitude', 'longitude', 'description', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }
    

