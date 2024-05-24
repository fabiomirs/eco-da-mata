from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def get_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', context={'projects':projects})