from django.db import models
from django.db.models import Q


class Category(models.Model):

    title = models.CharField(max_length = 30)

    def __str__(self):
        return self.title

    @classmethod
    def get_categories_by_ids(cls,ids):
        
        q = Q()
        
        for id in ids:

            q |= Q(id=id)
        
        categories = cls.objects.filter(q)
        print('-------------------------------------------------------')
        print(categories)
        return categories

