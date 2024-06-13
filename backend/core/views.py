from django.shortcuts import render
from rest_framework import viewsets
from .models import Imagem
from .serializers import ImagemSerializer
# Create your views here.

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer