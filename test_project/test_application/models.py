from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

class User(models.Model):
    name = models.TextField()
    email = models.EmailField()