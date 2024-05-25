from django import forms
from community_app.models import Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ["name", "link", "latitude", "longitude", "description","category", "logo"]
