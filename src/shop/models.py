from django.db import models
from django.contrib.postgres.fields import JSONField

from datetime import datetime 

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return("#{} {}".format(self.id, self.name))



# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    data = JSONField(null=True)
    # car_model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='items', null=True)

    def __str__(self):
        return "#{} {} ".format(self.id, self.name)


class Review(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews', null=True)
    datetime = models.DateTimeField(null=False, default=datetime.now())

    def __str__(self):
        return "#{}. ({}) {}".format(self.id, self.item.name, self.text)


class Image(models.Model):
    '''
    Object that references an image for different other models
    '''
    image = models.FileField(upload_to='hubImages/', blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')

