from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Fashion', 'Fashion'),
        ('Home', 'Home'),
        ('Books', 'Books'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name