from django import forms
from .models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['ccode','cname', 'coursefee', 'duration', 'prereq']
        # fields = '__all__'

class CourseAdd(forms.Form):
    ccode = forms.IntegerField(label="Course Code")
    cname = forms.CharField(label="Course Name", max_length = 20)
    coursefee = forms.IntegerField(label="Course Fee")
    duration = forms.CharField(label="Course Duration", max_length = 4)
    prereq = forms.CharField(label="Pre-Requisites", max_length = 100, widget=forms.Textarea)