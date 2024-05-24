from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_projects),
    path('<int:pk>', get_single_project)
]
