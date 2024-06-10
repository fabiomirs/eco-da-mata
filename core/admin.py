from django.contrib import admin
from .models import Imagem
from community_app.models import Community
from event_app.models import Event
from people_app.models import People
from project_app.models import Project

class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1


class CommunityAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]


class EventAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]


'''
class PeopleAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]'''


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]


admin.site.register(Community, CommunityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
#admin.site.register(People, PeopleAdmin)
