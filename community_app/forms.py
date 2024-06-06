from django import forms
from .models import Community, News






class CommunityForm(forms.ModelForm):
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

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'link', 'text', 'date', 'category', 'community_key']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'community_key': forms.Select(attrs={'class': 'form-control'}),
        }
    
