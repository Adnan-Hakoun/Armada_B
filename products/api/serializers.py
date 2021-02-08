from rest_framework import serializers
from products.models import Product
from categories.models import Category
import json

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product

        fields = '__all__'

        read_only_fields = ['owner','categories']

    def validate_price(self, value):
        
        if int(value)<=0 :
            raise serializers.ValidationError("Price cant be negative")
        return value

    def create(self, validated_data):
        str_ids = self.context['request'].data['categories'] #this is to have the data in case of many to many because many to many needs 2 instances and the validated data dosen send the infos of many to many. 
        ids = json.loads(str_ids)
        new_product = super().create(validated_data) # it will return instance with empty categories because its many to many field and its null=True by default
        categories = Category.get_categories_by_ids(ids)
        for cat in categories:
            new_product.categories.add(cat) 
        return new_product


class ProductsSerializerUpdate(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:

        model = Product

        exclude = ['owner','created_at']       