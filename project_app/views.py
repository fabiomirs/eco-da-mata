from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def get_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', context={'projects':projects})

def get_single_project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'single_project.html', context={'project':project})


def create_project(request):
    if request.method == 'POST':
        new_project = ProjectForm(request.POST, request.FILES)
        if new_project.is_valid():
            new_project.save()
        return redirect('all_projects')
    else:
        new_project = ProjectForm()
        return render(request, 'forms/new_project.html', {'new_project':new_project})
    