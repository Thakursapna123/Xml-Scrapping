from django.contrib import admin
from .models import Person, Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Person)