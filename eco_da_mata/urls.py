from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comunidade/', include('community_app.urls')),
    path('projetos/', include('project_app.urls')),
    path('events/', include('event_app.urls')),
    path('pessoas/',include('people_app.urls')),
    path('subcategoria',include('subcategory_app.urls'))
]
