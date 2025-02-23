from django.db import models


class Supplier(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):

        return self.name