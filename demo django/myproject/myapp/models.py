from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    place  = models.CharField(max_length=100)
    contact = models.IntegerField()



class Studenta(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField()
    batch = models.CharField(max_length=100)


    
