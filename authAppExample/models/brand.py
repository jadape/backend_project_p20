from django.db import models
from django.db.models.base import Model

class Brand(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField('brandname', max_length=15, unique=True)