from django.contrib import admin
from django.urls import path
from .views import registred_communities, single_community, community_create

urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('create/', community_create, name="communit_create"),
    path('<int:id>', single_community, name='single_community' )
]