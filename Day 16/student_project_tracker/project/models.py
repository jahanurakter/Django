from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    student_id=models.CharField(max_length=50,null=True)
    student_name=models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.student_id}-{self.student_name}"

class ProjectModel(models.Model):
    PROJECT_STATUS=[
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ]
    project_name=models.CharField(max_length=150, null=True)
    project_description=models.TextField(null=True)
    project_image=models.ImageField(upload_to='media/project_img', null=True)
    project_status=models.CharField(choices=PROJECT_STATUS,max_length=20, null=True)
    created_by=models.ForeignKey(UserModel,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.project_name}"