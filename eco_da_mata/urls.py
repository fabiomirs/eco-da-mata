from django.contrib import admin
from django.urls import path, include
from eco_da_mata import settings
from rest_framework.routers import DefaultRouter
from community_app.views import CommunityViewSet, NewsViewSet
from project_app.views import ProjectViewSet
from event_app.views import EventViewSet
from django.conf.urls.static import static
from people_app.views import PeopleViewSet, SubcategoryViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter() #Cria rotas automáticas para ViewSets (listagem, detalhamento)


router.register('project/', ProjectViewSet)
router.register('community', CommunityViewSet)
router.register('news', NewsViewSet)
router.register('people/', PeopleViewSet)
router.register('Event/', EventViewSet)
router.register('subcategory/', SubcategoryViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Eco da mata API",
        default_version="v1",
        description="Documentação da API do projeto Eco da mata mobile app",
        terms_of_service="http://admin.site.urls/terms/", #verificar se o site é esse mesmo
        contact=openapi.Contact(email=""), #falta adicionar e-mail
        license=openapi.License(name=""), #falta adicionar licensa
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<formats>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('community/', include('community_app.urls')),
#    path('projetos/', include('project_app.urls')),
#    path('events/', include('event_app.urls')),
#    path('pessoas/',include('people_app.urls')),
#    path('subcategoria',include('subcategory_app.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))


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
