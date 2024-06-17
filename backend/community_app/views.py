from .models import Community, News
from .serializers import CommunitySerializer, NewsSerializer
from rest_framework import viewsets

class CommunityViewSet(viewsets.ReadOnlyModelViewSet):  
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
