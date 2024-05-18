from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    class Category(models.TextChoices):
        LECTURE = 'LC', 'Lecture'
        FAIR = 'FR', 'Fair'
        CONFERENCE = 'CF', 'Conference'
        WORKHSOP = 'WK', 'Workshop'
        SEMINARY = 'SM', 'Seminary' 
        ART_EXHIBITION = 'AE', 'Art Exhibition' 
        FESTIVAL = 'FV', 'Festival'
        OTHERS = 'OT', 'Others'
    category = models.CharField(choices=Category.choices, default=Category.OTHERS)
    adress = models.CharField(max_length=75, blank=True, null=True)
    location = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    class Format(models.TextChoices):
        IN_PERSON = 'IP', 'IN_PERSON',
        ONLINE = 'ON', 'ONLINE',
        HYBRID = 'HB', 'HYBRID'
    value = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    pix_key = models.CharField(max_length=77, blank=True, default='')
    pix_key_owner = models.CharField(max_length=50, blank=True, default='')
    bank_name = models.CharField(max_length=25, blank=True, default='')
    pdf_link = models.URLField(blank=True, null=True, unique=True)
    questionary_link = models.URLField(blank=True, null=True, unique=True)
    profile_picture = models.ImageField(upload_to='images/events/profile_pictures')
    project_FK = models.ForeignKey(to="project_app.Project", on_delete = models.CASCADE) #Waiting project model to be defined