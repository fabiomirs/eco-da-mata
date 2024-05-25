from django.contrib import admin
from django.urls import path, include
from .views import registred_communities, single_community, community_create, news_create


urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('criar/', community_create , name="create_community"),
    path('noticia/criar', news_create, name='create_news' ),
    path('<int:id>', single_community, name='single_community' ) # Entrada de dados da URL -> VIEW
]