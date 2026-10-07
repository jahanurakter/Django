from django.db import models

class StuModel(models.Model):
    SELECT=[
        ('Science','Science'),
        ('Commerce','Commerce'),
        ('Arts','Arts'),
    ]
    stu_name=models.CharField(max_length=150, null=True)
    stu_class=models.CharField(max_length=50, null=True)
    stu_roll=models.PositiveIntegerField(null=True)
    stu_image=models.ImageField(upload_to='media/stu_image', null=True)
    select=models.CharField(choices=SELECT, max_length=50, null=True)
    publish_date=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.stu_name}"