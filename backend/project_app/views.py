from django.shortcuts import render, redirect
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProjectSerializer
from .models import Project
from .forms import ProjectForm

# Create your views here.

class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def get_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects':projects})

def get_single_project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'single_project.html', {'project':project})


def create_project(request):
    if request.method == 'POST':
        new_project = ProjectForm(request.POST, request.FILES)
        if new_project.is_valid():
            new_project.save()
        return redirect('all_projects')
    else:
        new_project = ProjectForm()
        return render(request, 'forms/new_project.html', {'new_project':new_project})
    
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('all_projects')
    else:
        project = Project.objects.get(id=pk)
        return render(request, 'delete_project.html', {'project':project})

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project_update = ProjectForm(request.POST, request.FILES, instance=project)
        if project_update.is_valid():
            project_update.save()
            return redirect('all_projects')
    else:
        project_update = ProjectForm(instance=project)
    return render(request, 'forms/update_project.html', {'project_update':project_update})
