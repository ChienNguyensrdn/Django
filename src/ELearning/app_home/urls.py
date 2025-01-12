from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('edit-course/<int:id>', views.edit_course, name='edit-course'),
    path('delete-course/<int:id>', views.delete_course, name='delete-course'),
    path('students', views.students, name='students'),
    path('student-edit/<int:id>', views.studentEdit, name='student-edit'),
    path('student-delete/<int:id>', views.studentDelete, name='student-delete'),
    path('student-new', views.studentNew, name='student-new'),
    path('course-new', views.CourseNew, name='course-new'),
    path('course-search', views.search_courses, name='course-search'),
]