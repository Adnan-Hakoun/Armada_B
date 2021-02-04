from django.db import models
from django.contrib.auth.models import AbstractUser


class Usery(AbstractUser):

    age = models.IntegerField(null=True)

    def __str__(self):
        
        return self.username +' / '+ str(self.age)

    @classmethod
    def get_current_user(cls,request):

        current_user =  cls.objects.get(id=request.user.id) 

        return current_user               
