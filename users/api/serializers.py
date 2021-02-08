from rest_framework import serializers
from users.models import Usery
from baskets.models import Basket


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        newuser = Usery.objects.create(username=validated_data['username'],
                                        age=validated_data['age'],
                                        type = validated_data['type'])
        newuser.set_password(validated_data['password'])
        newuser.save()
        Basket.objects.create(owner = newuser)
        return newuser
        

    class Meta:
        model = Usery
        
        fields = '__all__'
