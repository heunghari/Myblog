from django.db import models

# Create your models here.

class About(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField(upload_to='media/')
	body = models.TextField()

	def __str__(self):
		return self.title

