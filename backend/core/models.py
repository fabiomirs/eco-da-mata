from django.db import models
from community_app.models import Community
from event_app.models import Event
from people_app.models import People
from project_app.models import Project

class Imagem(models.Model):
    image = models.ImageField(upload_to='images/')
    community = models.ForeignKey(Community, null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    people = models.ForeignKey(People, null=True, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    entity = models.CharField(max_length=50, choices=[('community', 'Community'), ('event', 'Event'), ('people', 'People'), ('project', 'Project')])

    def save(self, *args, **kwargs):
        if self.community:
            self.entity = 'community'
        elif self.event:
            self.entity = 'event'
        elif self.people:
            self.entity = 'people'
        elif self.project:
            self.entity = 'project'
        super(Imagem, self).save(*args, **kwargs)