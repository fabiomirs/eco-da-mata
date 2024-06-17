from django.db import models
from people_app.models import People

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    social_network_link = models.URLField(max_length=200)
    telephone_number = models.CharField(max_length=20) # perhaps we can use 'django-phonenumber-field' extension.
    email = models.EmailField(max_length=254)
    community_key = models.ForeignKey(to="community_app.Community", on_delete=models.CASCADE) 
    people = models.ManyToManyField(People)

    def __str__(self):
        return self.name
    
