from django import forms


class StudentNewForm(forms.Form):
    code = forms.CharField(label="code", max_length=100)

class CourseNewForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    year = forms.IntegerField(label="year", min_value=1995)
    startDate = forms.DateField(label="startDate")
    endDate = forms.DateField(label="endDate")
    active = forms.BooleanField(label="active")