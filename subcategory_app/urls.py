from django.urls import path
from .views import SubcategoryList, UniqueSubcategory, SubcategoryCreate


path('subcategoria/', SubcategoryList.as_view(), name = 'subcategory_list'),
path('people/<int:pk>/', UniqueSubcategory.as_view(), name='subcategory_unique'),
path('criar/', SubcategoryCreate.as_view(), name = 'subcategory_regiser'),