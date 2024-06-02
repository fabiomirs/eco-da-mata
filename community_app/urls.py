from django.contrib import admin
from django.urls import path, include
from .views import registred_communities, single_community,news_update,news_detail, community_create, community_delete,news_create,community_update,news_delete
from .views import registred_communities, registred_tourist_spot, single_community,news_update,news_detail, community_create, community_delete,news_create,community_update


urlpatterns = [
    path('get/all/', registred_communities, name="registred_communities"),
    path('get/all/tourist_spot', registred_tourist_spot, name="registred_tourist_spot"),
    path('create/', community_create , name="create_community"),
    path('delete/<int:id>/', community_delete, name="delete_community"),
    path('put/<int:id>/', community_update, name='update_community'),
    path('news/create/', news_create, name='create_news' ),
    path('news/put/<int:id>/', news_update, name='update_news' ),
    path('news/get/<int:id>/', news_detail, name='detail_news' ),
    path('get/<int:id>/', single_community, name='single_community' )
]