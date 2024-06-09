from django.shortcuts import render, redirect
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProjectSerializer
from .models import Project
from .forms import ProjectForm

# Create your views here.


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

