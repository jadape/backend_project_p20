from django.db import models


class Product(models.Model):

    id          = models.AutoField(primary_key=True)
    name        = models.CharField('Productname', max_length=15, unique=True)
    description = models.CharField('Description', max_length=30, unique=False)
    price       = models.IntegerField(default=0)
    amount      = models.IntegerField(default=0)