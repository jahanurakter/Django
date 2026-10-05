from django.db import models

class CourseModel(models.Model):
    CATEGORY=[
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('CIVIL', 'CIVIL'),
    ]
    course_name=models.CharField(max_length=150,null=True)
    description=models.TextField(null=True)
    course_image=models.ImageField(upload_to='media/course_image', null=True)
    category=models.CharField(choices=CATEGORY, max_length=100, null=True)
    course_fee=models.PositiveIntegerField(null=True)
    def __str__(self):
        return f"{self.author_name}"
