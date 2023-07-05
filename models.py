from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083, default="image.jpg")


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
