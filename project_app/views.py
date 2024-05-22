from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_projects(request):
    return render(request, 'projects.html')