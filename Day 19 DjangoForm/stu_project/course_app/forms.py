from django import forms
from course_app.models import *

class StuForm(forms.ModelForm):
    class Meta:
        model = StuModel
        fields = '__all__'
     