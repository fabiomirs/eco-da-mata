from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comunidade/', include('community_app.urls')),
    path('projetos/', include('project_app.urls')),
    path('eventos/', include('event_app.urls')),
]
