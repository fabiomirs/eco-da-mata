from django.db import models

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=100, choices=(('COMMUNITY', 'Comunidade'),('TOURIST SPOT', 'Ponto Turístico')), default='COMMUNITY')
    logo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "communities"
        

class News(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100)
    #on_delete = models.CASCADE deleta todas as notícias associadas às comunidades excluídas
    community_key = models.ForeignKey(Community, on_delete=models.CASCADE, limit_choices_to={'category': 'COMMUNITY'})

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title