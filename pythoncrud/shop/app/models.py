from ast import mod
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.first_name


