from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from app_admin.models import Course, Student
from .forms import StudentNewForm, CourseNewForm
from django.core.cache import cache
from elasticsearch_dsl import Q
from app_admin.document import CourseDocument
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache trong 15 phút

def home(request):
    return render(request, 'home.html')
def clear_cache(request):
    cache.delete('courses')  # Xóa cache theo key
def courses(request):
  courses = cache.get('courses') # tim kiem data theo key: courses
  if not courses:
      # Nếu không có, tạo dữ liệu và lưu vào cache
      courses = Course.objects.all()
      cache.set('courses', courses, timeout=60*3)  # Lưu cache trong 60 giây
  

  template = loader.get_template('app_home/course/courses.html')
  context = {
    'courses': courses,
  }
  return HttpResponse(template.render(context, request))

def edit_course(request, id):
  if request.method == "POST":
    pass
  course = Course.objects.get(id = id)
  template = loader.get_template('app_home/course/course-edit.html')
  context = {
    'course': course,
  }
  return HttpResponse(template.render(context, request))

def search_courses(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        q = Q("multi_match", query=query, fields=["name", "description"])
        search = CourseDocument.search().query(q)
        results = search.execute()

    return render(request, 'app_home/course/search_results.html', {'results': results, 'query': query})


def delete_course(request, id):
  if request.method == "POST":
    pass
  course = Course.objects.get(id = id)
  template = loader.get_template('app_home/course/course-delete.html')
  context = {
    'course': course,
  }
  return HttpResponse(template.render(context, request))

def students(request):
  students = Student.objects.all()
  template = loader.get_template('app_home/student/students.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))

def studentEdit(request, id):
  student = Student.objects.get(id = id)
  courses =  student.courses.all
  # print("++++++++++++==========+++++++++++++",courses)
  template = loader.get_template('app_home/student/student-edit.html')
  context = {
    'student': student,
    'courses': courses,
  }
  return HttpResponse(template.render(context, request))

def studentDelete(request, id):
  if request.method == "POST":
    student = Student.objects.get(id = id)
    # student.delete()
    student.active =False
    student.save()
    return HttpResponseRedirect("/students")
  student = Student.objects.get(id = id)
  courses =  student.courses.all
  # print("++++++++++++==========+++++++++++++",courses)
  template = loader.get_template('app_home/student/student-delete.html')
  context = {
    'student': student,
    'courses': courses,
  }
  return HttpResponse(template.render(context, request))


def studentNew(request):
  if request.method == "POST":

    form = StudentNewForm(request.POST)
    # print(form)
    # student = Student.objects.get(id = id)
    # # student.delete()
    # student.active =False
    # student.save()
    return HttpResponseRedirect("/students")
  # student = Student.objects.get(id = id)
  # courses =  student.courses.all
  # print("++++++++++++==========+++++++++++++",courses)
  template = loader.get_template('app_home/student/student-new.html')
  context = {
    
  }
  return HttpResponse(template.render(context, request))

def CourseNew(request):
  if request.method == "POST":
    # get data to reponse 
    form = CourseNewForm(request.POST)
    print(form)
    # logic 
    if form. is_valid() :
      # commit database 
      return HttpResponseRedirect("/courses")
    # 

  template = loader.get_template('app_home/course/course-new.html')
  context = {
    
  }
  return HttpResponse(template.render(context, request))