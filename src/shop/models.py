from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	# brand = models.CharField()
	car_brand = models.CharField(max_length=100)
	car_model = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()

	def __str__(self):
		return "#{} {} ".format(self.id, self.name)