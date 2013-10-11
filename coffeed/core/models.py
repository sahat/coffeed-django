from django.db import models


class TimeStampedModel(models.Manager):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(TimeStampedModel):
    title = models.CharField(max_length=200)


class Order(TimeStampedModel):
    pass

