from django.core.urlresolvers import reverse
from django.db import models


class TimeStampedModel(models.Manager):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(TimeStampedModel):
    title = models.CharField(max_length=200)


class Order(TimeStampedModel):
    pass


class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})