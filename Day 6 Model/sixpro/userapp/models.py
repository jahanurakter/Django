from django.db import models

class info(models.Model):
    name=models.CharField(max_length=180,verbose_name="Student Name")
    address=models.TextField()
    email=models.EmailField()
    age=models.PositiveIntegerField()

class student(models.Model):
    name=models.CharField(max_length=180)
    roll=models.PositiveIntegerField()
    section=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}-{self.roll}-{self.section}"

class course(models.Model):
    title=models.CharField(max_length=255)
    dept=models.CharField(max_length=150)



