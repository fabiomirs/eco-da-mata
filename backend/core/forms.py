from django import forms
from .models import Imagem



class ImageForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }