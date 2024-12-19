from django.urls import path
from .views import RecipeViewSet, RecipeList, RecipesDetail
from rest_framework.routers import DefaultRouter




urlpatterns = [
    
    path('', RecipeList.as_view(), name='recipes_list'),
    path('<int:pk>/', RecipesDetail.as_view(), name='recipes_detail'),
]
