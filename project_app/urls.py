from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('my-api', ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', get_all_projects, name='all_projects'),
    path('<int:pk>', get_single_project, name='single_project'),
    path('criar/', create_project, name='new_project'),
    path('apagar/<int:pk>', delete_project, name='delete_project'),
    path('atualizar/<int:pk>', update_project, name='update_project')
]
