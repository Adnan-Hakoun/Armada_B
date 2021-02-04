from .serializers import UserSerializer 
from rest_framework import viewsets
from users.models import Usery
from rest_framework.decorators import action
from rest_framework.response import Response 


class UserViewSet(viewsets.ModelViewSet):

    queryset = Usery.objects.all()

    serializer_class = UserSerializer


    def get_authenticators(self):
    
        if self.request.method == "POST":

            return[]

        return [auth() for auth in self.authentication_classes]

    # @action(methods=['get'],detail = False) #to get current user as object
    # def current_user(self,request):
    #     current_user = request.user
    #     serializer = UserSerializer(current_user)
    #     return Response(serializer.data)

    @action(methods=['get'],detail = False) #this is to get current user infos and get his basket id
    def current_user(self,request):
        current_user = request.user
        
        basket = current_user.basket_set.first() 
        
        return Response({
            'username': current_user.username,
            'id' : current_user.id,
            'basket' : basket.id
        })

    