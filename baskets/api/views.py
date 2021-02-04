from .serializers import BasketsSerializer 
from rest_framework import viewsets
from baskets.models import Basket
from rest_framework.decorators import action 
from products.models import Product 
from rest_framework.response import Response 
from rest_framework import status 

class BasketsViewSet(viewsets.ModelViewSet):
    
    serializer_class = BasketsSerializer

    queryset = Basket.objects.all()

    @action(methods=['post'],detail = False) #@action adds url automatically.
    #(detail = False) will not  add "id/the name of the method" in url
    def add_products_to_basket(self,request) : #this is custom function just to add products to basket
        user = request.user 
        basket = user.basket_set.first() #for reverce relation in foriegn and many to many
        product_id = request.data.get("product_id")
        product = Product.objects.get(id = product_id)
        basket.products.add(product)
        return Response(1)

    #  @action(methods=['post'],detail = True) #@action adds url automatically.
    # #(detail = True) will add "id/the name of the method" in url
    # def add_products_to_basket(self,request,pk) : #this is custom function just to add products to basket
    #     basket = Basket.objects.get(id = pk) #pk is the id the system adds to url 
    #     product_id = request.data.get("product_id")
    #     product = Product.objects.get(id = product_id)
    #     basket.products.add(product)
    #     return Response(1)
     

    def get_queryset(self):

        if self.request.GET.get('basket_id'):

            basket_id = self.request.GET.get('basket_id')

            my_basket = Basket.objects.filter(id=basket_id)

            qs = my_basket 

        else:

            qs = Basket.objects.all() 

        return qs
        



    