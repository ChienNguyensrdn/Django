from django.db import models

# Create your models here.
class Course (models.Model):
    name = models.CharField(max_length= 50)
    startDate = models.DateField()
    endDate = models.DateField()
class Student(models.Model):
    fullName = models.CharField(max_length= 100)
    code = models.CharField(max_length= 12)
    gender = models.BooleanField()
    # Xac dinh moi quan he 
    courses = models.ManyToManyField(Course)

# Khai niem , logic ===>
