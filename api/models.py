from django.db import models
from datetime import datetime

# Create your models here.
class Record(models.Model):
	
	name_of_fish = models.CharField(max_length=50)
	species = models.CharField(max_length=50)
	weight = models.DecimalField(max_digits=10, decimal_places=3)
	length = models.DecimalField(max_digits=10, decimal_places=2)
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	timestamp = models.DateField(default=datetime.now().date())
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name_of_fish