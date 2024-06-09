from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProjectSerializer
from .models import Project


# Create your views here.


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

