from django.db import models

# Create your models here.
class category(models.Model):
    Category = models.CharField(max_length=20)

class products(models.Model):
    Category = models.ForeignKey(category, on_delete=models.PROTECT)
    Product = models.CharField(max_length=20)
    Price = models.IntegerField()
    Quantity = models.SmallIntegerField()
    Description = models.CharField(max_length=100)
