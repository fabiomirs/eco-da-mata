from django.contrib import admin
from django.urls import path, include
from .views import communit_list

urlpatterns = [
    path('', communit_list, name="communit_list"),
]
