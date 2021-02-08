from rest_framework import serializers
from categories.models import Category

class CategoriesSerizer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'