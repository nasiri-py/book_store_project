from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)  # price -> decimal

    def __str__(self):
        return self.title