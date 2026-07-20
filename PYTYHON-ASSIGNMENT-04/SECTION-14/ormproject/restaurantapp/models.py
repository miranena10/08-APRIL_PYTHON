from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=100)

    cuisine = models.CharField(max_length=50)

    rating = models.FloatField()

    def __str__(self):
        return self.name
    
 


class Movie(models.Model):

    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):

    movie=models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    review=models.TextField()

class Category(models.Model):

    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name=models.CharField(max_length=100)

    price=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name