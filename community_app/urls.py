from django.contrib import admin
from django.urls import path, include
from .views import registred_communities, single_community

urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('<int:id>', single_community, name='single_community' )
]
