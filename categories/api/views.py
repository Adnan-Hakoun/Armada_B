from .serializers import CategoriesSerizer
from categories.models import Category
from rest_framework import viewsets

class CategoriesViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriesSerizer

    queryset = Category.objects.all()