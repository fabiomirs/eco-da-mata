from django.contrib import admin
from django.urls import path, include
from .views import registred_communities, single_community,news_update,news_detail, community_create, community_delete,news_create,community_update


urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('criar/', community_create , name="create_community"),
    path('deletar/<int:id>', community_delete, name="delete_community"),
    path('atualizar/<int:id>/', community_update, name='update_community'),
    path('noticia/criar', news_create, name='create_news' ),
    path('noticia/atualizar/<int:id>', news_update, name='update_news' ),
    path('noticia/visualizar/<int:id>', news_detail, name='detail_news' ),
    path('<int:id>', single_community, name='single_community' ) # Entrada de dados da URL -> VIEW
]