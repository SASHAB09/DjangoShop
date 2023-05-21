from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    img_url = models.CharField(max_length=200, default=None)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

class CartItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
