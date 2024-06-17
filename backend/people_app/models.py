from django.db import models


class Subcategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=[('institution', 'Institution'), ('physical person', 'Physical person')])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    institutional_email = models.EmailField(max_length=100, unique=True)
    personal_page_link = models.URLField(max_length=200, blank=True, null=True)
    logo = models.ImageField(blank=True, upload_to="images/")
    category = models.CharField(max_length=20, choices=[('institution', 'Institution'), ('physical person', 'Physical person')])
    subcategory_key = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




