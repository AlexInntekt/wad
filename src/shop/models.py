from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    data = JSONField(null=True)
    # car_model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return "#{} {} ".format(self.id, self.name)


class Image(models.Model):
    '''
    Object that references an image for different other models
    '''
    image = models.FileField(upload_to='hubImages/', blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
