from django.db import models

class DeptModel(models.Model):
    dept_name=models.CharField(max_length=150, null=True)
    d_description=models.TextField(null=True)
    dept_head=models.CharField(max_length=150, null=True)

class CourseModel(models.Model):
    course_title=models.CharField(max_length=150, null=True)
    c_description=models.TextField(null=True)
    course_image=models.ImageField(upload_to="media/course_img", null=True)

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=150, null=True)
    stu_image=models.ImageField(upload_to="media/stu_img", null=True)
    admission_date=models.DateField(null=True)
    course_name=models.CharField(max_length=150, null=True)
    course_fee=models.PositiveIntegerField(null=True)

class TeacherModel(models.Model):
    teacher_name=models.CharField(max_length=150, null=True)
    email=models.EmailField(null=True)
    phone_number=models.PositiveIntegerField(null=True)

class ResultModel(models.Model):
    stu_name=models.CharField(max_length=150, null=True)
    marks=models.PositiveIntegerField(null=True)
    grade=models.CharField(max_length=2, null=True)