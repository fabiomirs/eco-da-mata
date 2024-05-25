from django.urls import path
from .views import PeopleList, PeopleDetails


urlpatterns = [
    path('people/', PeopleList.as_view(), name = 'people_list'),
    path('people/<int:pk>/', PeopleDetails.as_view(), name='people_detail')
]
