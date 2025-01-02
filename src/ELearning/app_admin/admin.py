from django.contrib import admin
from .models import Course, Student
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
  list_display = ("name", "year", "startDate","endDate","active")


class StudentAdmin(admin.ModelAdmin):
  list_display = ("code","fullName", "birthDay", "active")

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)