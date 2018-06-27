from django.db import models

# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=100,blank=True,null=True)
	lastname=models.CharField(max_length=100,blank=True,null=True)
	def __str__(self):
		return u"%s"%(self.name)

