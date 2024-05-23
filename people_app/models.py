from django.db import models
#from subcategory_app.models import Subcategory


    
class People(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    institutional_email = models.EmailField(max_length=100)
    personal_page_link = models.URLField(max_length=200)
    #logo = models.ImageField(upload_to='people_logos/', blank=True)
    category = models.CharField(max_length=20, choices=[('institution', 'Institution'), ('physical person', 'Physical person')])
    #subcategory_key = models.ForeignKey(Subcategory, on_delete=models.CASCADE,default=1)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 
    people_fk = models.ForeignKey('People', on_delete=models.CASCADE,default=1)