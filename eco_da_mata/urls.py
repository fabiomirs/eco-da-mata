from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from community_app.views import CommunityViewSet, NewsViewSet
from project_app.views import ProjectViewSet
from people_app.views import PeopleViewSet


router = DefaultRouter() #Cria rotas automáticas para ViewSets (listagem, detalhamento)

router.register('project/', ProjectViewSet)
router.register('community', CommunityViewSet)
router.register('news', NewsViewSet)
router.register('people/', PeopleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community_app.urls')),
    path('projetos/', include('project_app.urls')),
    path('events/', include('event_app.urls')),
    path('pessoas/',include('people_app.urls')),
    path('subcategoria',include('subcategory_app.urls'))
]
"""