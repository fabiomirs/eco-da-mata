from django.urls import path
from .views import SubcategoryList, UniqueSubcategory, SubcategoryCreate, SubcategoryDelete
from .views import SubcategoryUpdate



urlpatterns = [
path('subcategoria/', SubcategoryList.as_view(), name = 'subcategory_list'),
path('subcategoria/<int:pk>/', UniqueSubcategory.as_view(), name='subcategory_unique'),
path('criar/', SubcategoryCreate.as_view(), name = 'subcategory_register'),
path('deletar/<int:pk>/',SubcategoryDelete.as_view(), name = 'subcategory_delete'),
path('atualizar/<int:pk>/',SubcategoryUpdate.as_view(), name = 'subcategory_update'),
            ]