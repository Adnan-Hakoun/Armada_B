from rest_framework import serializers
from products.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product

        fields = '__all__'

        read_only_fields = ['owner']


class ProductsSerializerUpdate(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:

        model = Product

        exclude = ['owner','created_at']       