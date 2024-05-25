from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ("name", "description", "social_network_link", "telephone_number", "email", "community_key")
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'social_network_link':forms.TextInput(attrs={'class':'form-control'}),
            'telephone_number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'community_key':forms.Select(attrs={'class':'form-control'})
        }