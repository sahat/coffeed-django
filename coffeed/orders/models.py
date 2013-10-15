from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)


class Order(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    item = models.ManyToManyField(Item)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


