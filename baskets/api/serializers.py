from rest_framework import serializers
from baskets.models import Basket
from products.api.serializers import ProductsSerializer

class BasketsSerializer(serializers.ModelSerializer):

    products = ProductsSerializer(many=True)#many True because we want more than one product 

    class Meta:

        model = Basket

        fields = '__all__'
