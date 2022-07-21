from types import CoroutineType
from django.db import models

# Create your models here
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=100,default='')

class Person(models.Model):
    name=models.CharField(max_length=12)
    mobile=models.CharField(max_length=10)
    city=models.CharField(max_length=20)