from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def get_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', context={'projects':projects})

def get_single_project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'single_project.html', context={'project':project})