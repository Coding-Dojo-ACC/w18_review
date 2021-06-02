from django.db import models

class Item(models.Model):
    itemName=models.CharField(max_length=45)
    description=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2, max_digits=5)

class Order(models.Model):
    ordered=models.IntegerField()
    totalPrice=models.DecimalField(decimal_places=2, max_digits=7)