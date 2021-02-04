from django.db import models
from users.models import Usery
from products.models import Product

class Basket(models.Model):

    owner = models.ForeignKey(Usery,on_delete = models.CASCADE)

    products = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.owner.username+ ' / ' + str(self.id)