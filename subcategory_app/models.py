from django.db import models



class Subcategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=[('institution', 'Institution'), ('physical person', 'Physical person')])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title