from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_projects, name='all_projects'),
    path('<int:pk>', get_single_project, name='single_project'),
    path('criar/', create_project, name='new_project'),
    path('apagar/<int:pk>', delete_project, name='delete_project'),
    path('atualizar/<int:pk>', update_project, name='update_project')
]
