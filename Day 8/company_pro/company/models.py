from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=150)
    email = models.EmailField()
    position = models.CharField(max_length=100)

class dept(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()

