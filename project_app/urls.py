from django.urls import path
from .views import get_all_projects

urlpatterns = [
    path('', get_all_projects),
]
