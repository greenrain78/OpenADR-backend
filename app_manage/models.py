from django.db import models


# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)


class User(models.Model):
    AUTH_CHOICES = [('U', 'User'), ('A', 'Admin')]
    identification = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    auth = models.CharField(choices=AUTH_CHOICES, max_length=1)
    sites = models.ManyToManyField(Site)


class test_db(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField()
