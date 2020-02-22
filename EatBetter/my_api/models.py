from django.db import models

# Create your models here.


class Aliment(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(null=False)
    owner = models.ForeignKey('auth.User', related_name='aliments', on_delete=models.CASCADE)
    vitamin = models.CharField(max_length=5, null=True)
    glucose = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    lipid = models.IntegerField(null=True)
    minerals = models.IntegerField(null=True)

    def __str__(self):
        """A string representation of an aliment"""
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(null=False)
    owner = models.ForeignKey('auth.User', related_name='foods', on_delete=models.CASCADE)
    aliment = models.ManyToManyField(Aliment, through='Step', blank=True)

    def __str__(self):
        """A string representation of an aliment"""
        return self.name


class Step(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)