from django import forms
from course_app.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'