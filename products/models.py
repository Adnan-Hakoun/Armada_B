from django.db import models
from users.models import Usery
from categories.models import Category
from django.db.models import Q

class Product(models.Model):

    name = models.CharField(max_length = 120)

    price = models.DecimalField(max_digits = 8 , decimal_places = 2)

    categories = models.ManyToManyField(Category,blank=True)

    image = models.ImageField(upload_to = 'normal/%Y/%m/%d')

    owner = models.ForeignKey(Usery,on_delete=models.CASCADE)

    is_deleted = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):

        return self.name + ' / ' + str(int(self.price)) + ' / ' +self.owner.username

    @classmethod
    def search_by_name(cls , lst):

        names = lst.split(' ')

        q = Q()

        for name in names:

            q |= Q(name__icontains = name)

            products = cls.objects.filter(q).filter(is_deleted = False)

        return products

     