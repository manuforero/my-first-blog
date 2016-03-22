from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Receta(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 500)
	category = models.CharField(max_length = 100)
	instructions = models.TextField()
	image = models.ImageField(blank = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)
