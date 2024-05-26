from django.urls import path
from .views import PeopleList, PeopleDetails, PeopleCreate


urlpatterns = [
    path('people/', PeopleList.as_view(), name = 'people_list'),
    path('<int:pk>/', PeopleDetails.as_view(), name='people_detail'),
    path('criar/', PeopleCreate.as_view(), name = 'people_regiser'),
]
