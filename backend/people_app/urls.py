from django.urls import path
from .views import PeopleList, PeopleDetails, PeopleCreate, PeopleUpdate, PeopleDelete


urlpatterns = [
    path('pessoas/', PeopleList.as_view(), name = 'people_list'),
    path('pessoas/<int:pk>/', PeopleDetails.as_view(), name='people_detail'),
    path('criar/', PeopleCreate.as_view(), name = 'people_register'),
    path('atualizar/<int:pk>/', PeopleUpdate.as_view(), name = 'people_update'),
    path('delete/<int:pk>/', PeopleDelete.as_view(), name = 'people_delete')
]
