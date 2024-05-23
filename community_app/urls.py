from django.contrib import admin
from django.urls import path, include
from .views import registred_communities, single_community, CommunityCreate, NewsCreate

urlpatterns = [
    path('listar/', registred_communities, name="registred_communities"),
    path('criar/comunidade/', CommunityCreate.as_view(), name="communit_create"),
    path('criar/noticia/', NewsCreate.as_view(), name="news_create"),
    path('<int:id>', single_community, name='single_community' )
]