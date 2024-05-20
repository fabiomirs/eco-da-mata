from django.contrib import admin
from django.urls import path, include
from .views import community_list, community_unique

urlpatterns = [
    path('/', community_list, name="communit_list"),
    path('<int:id>/', community_unique, name="communit_list"),
]
