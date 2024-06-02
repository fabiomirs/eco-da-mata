from django.db import models
from ..community_app.models import Community
from ..event_app.models import Event
from ..people_app.models import People
from ..project_app.models import Project


# Create your models here.
class Imagem(models.Model):
    image = models.ImageField(upload_to='images/')
    community = models.ForeignKey(Community, null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)
    people = models.ForeignKey(People, null=True, blank=True)
    project = models.ForeignKey(Project, null=True, blank=True)
    entity = models.CharField(max_length=50, choices=[('community', 'Community'), ('event', 'Event'), ('people', 'People'), ('project', 'Project')])