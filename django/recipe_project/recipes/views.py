from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Recipes
from .serializers import RecipeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class RecipeViewSet(ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer



class RecipeList(ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer


class RecipesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer