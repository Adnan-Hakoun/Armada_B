from .serializers import ProductsSerializer , ProductsSerializerUpdate
from rest_framework import viewsets , permissions
from products.models import Product
from .permissions import IsVendorOrReadOnly



class ProductsViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductsSerializer

    queryset = Product.objects.filter(is_deleted = False)

    permission_classes = [IsVendorOrReadOnly]

    def get_queryset(self):
        
        if self.request.GET.get('keys'):

            keys = self.request.GET.get('keys')

            items = Product.search_by_name(keys) #function i created in the models.py

        else:

            items = Product.objects.filter(is_deleted = False) 

        return items
   

    def perform_create(self, serializer):
        
        serializer.save(owner = self.request.user)

    def get_serializer_class(self):
        
        if self.action == 'update':
            return ProductsSerializerUpdate
        return ProductsSerializer    

