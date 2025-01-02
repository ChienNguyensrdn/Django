from django.db import models
from django import forms
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 150)
    year = models.IntegerField(default= 2024)
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.BooleanField()
    def __str__(self):
        return f"{self.name} {self.year}"
    
class Student (models.Model):
    fullName = models.CharField(max_length= 255)
    birthDay = models.DateField()
    code = models.CharField(max_length= 12)
    courses = models.ManyToManyField(Course)
    active = models.BooleanField()
    def __str__(self):
        return f"{self.code} {self.fullName}"
    
