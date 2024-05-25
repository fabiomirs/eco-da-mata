from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    description = models.TextField(unique=True)
    class Category(models.TextChoices):
        LECTURE = 'LC', 'Lecture'
        FAIR = 'FR', 'Fair'
        CONFERENCE = 'CF', 'Conference'
        WORKHSOP = 'WK', 'Workshop'
        SEMINARY = 'SM', 'Seminary' 
        ART_EXHIBITION = 'AE', 'Art Exhibition' 
        FESTIVAL = 'FV', 'Festival'
        OTHERS = 'OT', 'Others'

    category = models.CharField(max_length=2, choices=Category.choices, 
                                default=Category.OTHERS)
    address = models.CharField(max_length=75, blank=True, null=True)
    location = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    class Format(models.TextChoices):
        IN_PERSON = 'IP', 'IN_PERSON',
        ONLINE = 'ON', 'ONLINE',
        HYBRID = 'HB', 'HYBRID'

    format = models.CharField(max_length=2, choices=Format.choices)
    value = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    pix_key = models.CharField(max_length=77, blank=True, default='')
    pix_key_owner = models.CharField(max_length=50, blank=True, default='')
    bank_name = models.CharField(max_length=25, blank=True, default='')
    pdf_link = models.URLField(blank=True, null=True, unique=True)
    questionary_link = models.URLField(blank=True, null=True, unique=True)
    profile_picture = models.ImageField()
    project_FK = models.ForeignKey(to="project_app.Project", on_delete = models.CASCADE)


class Review(models.Model):
    person_name = models.CharField(max_length=50)
    phrase = models.CharField(max_length=100)
    class Grade(models.IntegerChoices):
        GRADE_1 = 1
        GRADE_2 = 2
        GRADE_3 = 3
        GRADE_4 = 4
        GRADE_5 = 5
    
    grade = models.IntegerField(choices=Grade.choices)
    event_FK = models.ForeignKey(to=Event, on_delete=models.CASCADE)