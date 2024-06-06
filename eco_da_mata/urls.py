from django.contrib import admin
from django.urls import path, include
from eco_da_mata import settings
from rest_framework.routers import DefaultRouter
from project_app.views import ProjectViewSet
from django.conf.urls.static import static

router = DefaultRouter()
router.register('project/', ProjectViewSet)


urlpatterns = [
   # path('api/', include(router.urls)),
     path('admin/', admin.site.urls),
     path('community/', include('community_app.urls')),
#    path('projetos/', include('project_app.urls')),
#    path('events/', include('event_app.urls')),
#    path('pessoas/',include('people_app.urls')),
#    path('subcategoria',include('subcategory_app.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)