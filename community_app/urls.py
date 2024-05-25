from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from .views import registred_communities, single_community, create_community


urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('criar/', create_community , name="create_community"),
    #path('criar/noticia/', NewsCreate.as_view(), name="news_create"),
    path('<int:id>', single_community, name='single_community' ) # Entrada de dados da URL -> VIEW
=======
from django.urls import path
from .views import registred_communities, single_community, community_create

urlpatterns = [
    path('', registred_communities, name="registred_communities"),
    path('create/', community_create, name="communit_create"),
    path('<int:id>', single_community, name='single_community' )
>>>>>>> 7fb09240d14db6caefb0ca736cd0b59dd595ff76
]