from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    item = models.ManyToManyField(Item)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.location
